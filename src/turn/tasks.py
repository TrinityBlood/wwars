from celery import task


from turn.logic import turn_tick

@task
def turn_tick_task():
    turn_tick()
