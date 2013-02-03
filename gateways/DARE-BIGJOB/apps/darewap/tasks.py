from celery.decorators import task
from dare.core.dare_manager import DareManager
from darewap.models import Job, JobInfo, UserResource, UserTasks
from dare.helpers.cfgparser import CfgWriter
import os
from django.conf import settings

import bigjob
from pilot import PilotComputeService, PilotCompute, ComputeUnit, State
BIGJOB_DIRECTORY = "~/.bigjob/"

COORD_URL = "redis://cyder.cct.lsu.edu:2525/"


@task
def start_pilot(job_id, ur_id, coordination_url=COORD_URL):
    print job_id, ur_id
    job = Job.objects.get(id=job_id)
    pilot = job.get_pilot_with_ur(ur_id)
    #print pilot.detail
    # create pilot job service and initiate a pilot job
    pilot_compute_description = {"service_url": "fork://localhost",
                         "number_of_processes": 1,
                         "working_directory":  '/tmp/',
                         "number_of_processes": 1,
                         "processes_per_node": 1}

    #pilot_compute_description = pilot.detail

    #pilot_compute_description.update({"number_of_processes": 1,
    #                     "processes_per_node": 1,
    #                     "walltime": 16,
    #                     "project": "TG-MCB090174",
    #                     })
    #pilot_compute_description = dict([(k, str(v)) for k, v in pilot_compute_description.items()])

    #import pdb;pdb.set_trace()

    pilot_compute_description = {
                             "service_url": 'sge+ssh://smaddi2@ranger.tacc.utexas.edu',
                             "number_of_processes": 16,
                             "queue": "development",
                             "walltime": 10,
                             "allocation": "TG-MCB090174",
                             "working_directory": "/work/01395/smaddi2/dare/",
                             "affinity_datacenter_label": "eu-de-south",
                             "affinity_machine_label": "mymachine-1",
                            }

    pilot_compute_service = PilotComputeService(coordination_url=COORD_URL)
    pilot_compute = pilot_compute_service.create_pilot(pilot_compute_description=pilot_compute_description)
    pilot_url = pilot_compute.get_url()
    pilot.detail['pilot_url'] = pilot_url
    pilot.detail['status'] = "Submitted"
    pilot.save()
    print("Started Pilot: %s" % (pilot_url))


@task
def stop_pilot(job_id, ur_id, coordination_url=COORD_URL):

    job = Job.objects.get(id=job_id)
    pilot = job.get_pilot_with_ur(ur_id)
    print pilot.detail
    pilot_url = pilot.detail.get("pilot_url")
    #cancle
    pilot_compute = PilotCompute(pilot_url=pilot_url)
    pilot_compute.cancel()

    pilot.detail['pilot_url'] = ""
    pilot.detail['status'] = "Stopped"
    pilot.save()
    print("Started Pilot: %s" % (pilot_url))


@task
def get_pilot_status(job_id, ur_id, coordination_url=COORD_URL):

    job = Job.objects.get(id=job_id)
    pilot = job.get_pilot_with_ur(ur_id)
    pilot_url = pilot.detail.get("pilot_url")

    if pilot_url:
        pilot_compute = PilotCompute(pilot_url=pilot_url)

        if pilot.detail.get('status') == "Submitted":
            print pilot.detail.get('status')
            if pilot_compute.get_state() == State.Running:
                status = "Running"
                percentage = 100

            if pilot_compute.get_state() == State.New:
                status = "New"
                percentage = 0

            if pilot_compute.get_state() == State.Unknown:
                status = "Submitted"
                percentage = 30

        else:
            percentage = 0
            status = ""

        print pilot.detail['status'], percentage, status
        p = {'ur_id': ur_id, 'percentage': percentage, 'state': status}
        return p
    else:
        if pilot.detail.get('status') == "Stopped":
            return {'ur_id': ur_id, 'percentage': 0, 'state': "Stopped"}
        else:
            return {'ur_id': ur_id, 'percentage': 0, 'state': State.Unknown}


@task
def start_task(staskid):

    taskinfo = JobInfo.objects.get(id=int(staskid))
    pilot_url = taskinfo.job.get_pilot_url()
    ut_id = taskinfo.detail.get('ut_id')
    ut = UserTasks.objects.get(id=ut_id)
    env = {}
    env["locals"]   = None
    env["globals"]  = None
    env["__name__"] = None
    env["__file__"] = None
    env["__builtins__"] = None
    exec(ut.script)
    #import pdb;pdb.set_trace()

    cus = tasks()
    if pilot_url:
        pilot_compute = PilotCompute(pilot_url=pilot_url)
        for cu in cus:
            compute_unit_description = {
                    "executable": "/bin/date",
                    "arguments": [''],
                    "total_core_count": 1,
                    "number_of_processes": 1,
                    "output": "stdout.txt",
                    "error": "stderr.txt",
                }
            compute_unit = pilot_compute.submit_compute_unit(cu)
            print "Started ComputeUnit: %s" % (compute_unit.get_url())
            taskinfo.detail['cu_url'] = compute_unit.get_url()
            taskinfo.detail['status'] = 'Submitted'
            taskinfo.save()
        return compute_unit


@task
def get_task_status(staskid):

    taskinfo = JobInfo.objects.get(id=int(staskid))
    cu_url = taskinfo.detail.get('cu_url')
    percentage = taskinfo.detail.get('percentage', 0)
    status = taskinfo.detail['status']

    if cu_url:
        compute_unit = ComputeUnit(cu_url=cu_url)
        if compute_unit.get_state() == State.Running:
            status = "Running"
            percentage = 50

        elif compute_unit.get_state() == State.Done:
            status = State.Done
            percentage = 100
        else:
            if taskinfo.detail.get('status') == "Submitted":
                percentage = 20
                status = "Submitted"

        taskinfo.detail['status'] = status
        taskinfo.detail['percentage'] = percentage
        taskinfo.save()

    return {'staskid': staskid, 'percentage': percentage, 'state': status}
