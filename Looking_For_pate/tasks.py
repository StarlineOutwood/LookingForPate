from invoke import task

@task
def start(ctx):
    ctx.run("python3 src/run.py", pty=True)