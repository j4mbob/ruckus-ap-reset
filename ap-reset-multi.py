#!/usr/bin/env python2

import pexpect
import sys
import argparse
import logging
import multiprocessing
import time

def parseArguments():

    parser = argparse.ArgumentParser(description='Ruckus AP Reset')
    parser.add_argument('filepath', help='filepath')
    parser.add_argument('username',help='admin username on AP')
    parser.add_argument('password',help='admin password on AP')

    return parser.parse_args()
            

def spanwProcess(ruckus):

    logging.info("Process %s: starting", ruckus.ip)

    try:

        ruckus.child = pexpect.spawn('ssh -o StrictHostKeyChecking=no ' + ruckus.ip)
        ruckus.child.logfile = sys.stdout
        ruckus.child.timeout = 45
        ruckus.child.expect ('Please login:')
        ruckus.child.sendline (ruckus.username)
        ruckus.child.expect ('password : ')
        ruckus.child.sendline (rukus.password + "\r")
        ruckus.child.expect ('rkscli: ')
        ruckus.child.sendline('set factory\r')
        ruckus.child.expect ('OK')
        ruckus.child.sendline('reboot\r')
        ruckus.child.expect ('OK')

    except:

        logging.error("Process %s: an error occurred", ruckus.ip)

    logging.info("Process %s: finishing", ruckus.ip)

class Ruckus:


    def __init__(self, ip, username, password):

        self.ip = ip
        self.username = username
        self.password = password

if __name__ == '__main__':

    format = "%(asctime)s: %(message)s"

    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")

    args = parseArguments()

    logging.info("Main: parsing jobs")

    jobs = []

    with open(args.filepath) as file:
        for ip in file:
            rukus = Ruckus(ip, args.username, args.password)
            process = multiprocessing.Process(target=spanwProcess, args=(rukus,))
            jobs.append(process)

    logging.info("Main: starting %d jobs", len(jobs))

    for j in jobs:
        j.start()

    for j in jobs:
        j.join()

    logging.info("Main: finishing %d jobs", len(jobs))
