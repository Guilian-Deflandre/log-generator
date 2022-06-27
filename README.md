# Log Generator
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://GitHub.com/Naereen/StrapDown.js/graphs/commit-activity) [![Docker](https://badgen.net/badge/icon/docker?icon=docker&label)](https://https://docker.com/) [![Discord](https://badgen.net/badge/icon/discord?icon=discord&label)](https://discord.com/users/756143049779970158)

## Context

This project is used to generate randomly typical logs of an infrastructure and output them to a log file. The primary goal of this project was to feed a Logstash process first for debugging an Elasticsearch deployment, then to simulate the behavior of a log aggregator in a honeypot.

Logstash uses regular expressions (regex) to collect information from a log file. Since the purpose of this application is to create logs matched by a Logstash process using Grok regular expressions, these last have been used to design the different formats followed by the logs forged by the Log Generator. They can be viewed in the folder `/data/logstash_regex`.

## Structure

Fig. 1 gives the structure of the Log Generator application. This application is multi-threaded, a typical thread execution is illustrated in Fig. 2.

<figure>
<img src="/data/images/static_diagram.png" alt="Trulli" style="width:100%">
<figcaption align = "center"><b>Fig. 1 - Static Diagram of the Log Generator Application</b></figcaption>
</figure>

<figure>
<img src="/data/images/dynamic_diagram.png" alt="Trulli" style="width:100%">
<figcaption align = "center"><b>Fig. 2 - Dynamic Diagram of the Log Generator Application</b></figcaption>
</figure>

From Fig. 2, it can be see that each thread of the application manages several generators creating logs of different formats. These standard formats are defined in the `log_generator` package. The thread oscillate infinitely between a generation phase and a sleeping phase, writing at each loop iteration distinct logs randomly in the output log file.

Various data (such as IP addresses, usernames, etc.) in the logs have been generated using the [Faker](https://github.com/joke2k/faker) Python package. The functions relying on this package are located in the `utils.py` file.
