#!/usr/bin/env python3

import json
import subprocess

import pingparsing
import boto3

def test_host(hostname):

    cmd = 'sudo ping -i0.0 -c100 ' + hostname
    results = subprocess.run(cmd, capture_output=True, text=True, shell=True).stdout

    parser = pingparsing.PingParsing()
    stats = parser.parse(results)

    response = cloudwatch.put_metric_data(
        Namespace='PingTest',
        MetricData=[
            {
                'MetricName' : 'PacketLoss',
                'Unit' : 'Percent',
                'Value' : stats.packet_loss_rate,
                'Dimensions': [
                    {
                        'Name': 'Hostname',
                        'Value': hostname
                    },
                    {
                        'Name': 'Source',
                        'Value': 'Macallan'
                    },
                ]
            },
            {
                'MetricName' : 'RttMin',
                'Unit' : 'Milliseconds',
                'Value' : stats.rtt_min,
                'Dimensions': [
                    {
                        'Name': 'Hostname',
                        'Value': hostname
                    },
                    {
                        'Name': 'Source',
                        'Value': 'Macallan'
                    },

                ]
            },
            {
                'MetricName' : 'RttAvg',
                'Unit' : 'Milliseconds',
                'Value' : stats.rtt_avg,
                'Dimensions': [
                    {
                        'Name': 'Hostname',
                        'Value': hostname
                    },
                    {
                        'Name': 'Source',
                        'Value': 'Macallan'
                    },
                ]
            },
            {
                'MetricName' : 'RttMax',
                'Unit' : 'Milliseconds',
                'Value' : stats.rtt_max,
                'Dimensions': [
                    {
                        'Name': 'Hostname',
                        'Value': hostname
                    },
                    {
                        'Name': 'Source',
                        'Value': 'Macallan'
                    },
                ]
            },
            {
                'MetricName' : 'RttMdev',
                'Unit' : 'Milliseconds',
                'Value' : stats.rtt_mdev,
                'Dimensions': [
                    {
                        'Name': 'Hostname',
                        'Value': hostname
                    },
                    {
                        'Name': 'Source',
                        'Value': 'Macallan'
                    },
                ]
            },
        ]
    )


if __name__ == '__main__':
    cloudwatch = boto3.client('cloudwatch', region_name='us-east-1')
    test_host('ping.us-west-2.dougal.io')

