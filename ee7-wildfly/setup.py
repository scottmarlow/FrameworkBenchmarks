import subprocess
import sys
import setup_util
import os

def start(args, logfile, errfile):
  try:
    subprocess.check_call("mvn clean initialize package -Pbenchmark -Ddatabase.host=" + args.database_host, shell=True, cwd="ee7-wildfly", stderr=errfile, stdout=logfile)
    subprocess.Popen("target/wildfly-8.0.0.CR1/bin/standalone.sh -b 0.0.0.0", shell=True, cwd="ee7-wildfly", stderr=errfile, stdout=logfile)
    return 0
  except subprocess.CalledProcessError:
    return 1
def stop(logfile, errfile):
  try:
    subprocess.check_call("target/wildfly-8.0.0.CR1/bin/jboss-cli.sh --connect --command=:shutdown", shell=True, cwd="ee7-wildfly", stderr=errfile, stdout=logfile)
    return 0
  except subprocess.CalledProcessError:
    return 1
