import os
import time
import logging
import subprocess
import json

source_dir = '/incoming_images'
license_plate_dir = '/license_plates'
int i = 0


def handle_message():
    while True:
        incoming_images = os.listdir(source_dir)
        if len(incoming_images) == 0:
            print("No available image. Sleep 3 secs...")
            time.sleep(3)
        else:
            i = i + 1
            print(incoming_images[i])
            p = subprocess.Popen("/usr/bin/alpr -c us -n 1 -j " + source_dir +
                                 "/" + incoming_images[0], stdout=subprocess.PIPE, shell=True)
            (alpr_output_str, err) = p.communicate()
            p_status = p.wait()
            alpr_output = json.load(alpr_output_str)
            if len(alpr_output['results']) > 0:
                print(alpr_output['results'][0]["plate"])
                # p = subprocess.Popen("cp " + source_dir + "/" + incoming_images[0] + " " + license_plate_dir + "/" + license_plate_number)
                # time.sleep(2)
                # print("DELETE FILE : " + incoming_images[0])
                # os.unlink(incoming_images[0])


def create_daemon():
    """
        This function create a service/Daemon that will execute a det. task
    """

    try:
        # Store the Fork PID
        pid = os.fork()

        if pid > 0:
            print('PID: %d' % pid)
            os._exit(0)
    except OSError as error:
        print('Unable to fork. Error: %d (%s)' % (error.errno, error.strerror))
        os._exit(1)
    handle_message()


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s %(levelname)s %(message)s',
                        filename='licenseplate_monitor.log',
                        filemode='w')
    create_daemon()
