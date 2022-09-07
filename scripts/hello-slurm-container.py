import psij
import time
from pathlib import Path

# settings
timestamp = time.strftime("%Y-%m-%d-%H-%M-%S")
wd = Path('/data/.psij/')
log = Path('/data/launcher.log')
N = 2  # number of jobs to run

# create config and job executor
config = psij.JobExecutorConfig(launcher_log_file=log, work_directory=wd)
jex = psij.JobExecutor.get_instance('slurm', config=config)


# make job
job = psij.Job()
spec = psij.JobSpec()
spec.executable = 'hostname'
spec.arguments = []
spec.stdout_path = 'hostname.' + timestamp + '.stdout'
job.spec = spec

# submit job
jex.submit(job)
