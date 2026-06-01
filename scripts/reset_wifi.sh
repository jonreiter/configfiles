#!/bin/bash

DRIVER=ath11k_pci

modprobe -r ${DRIVER}
modprobe ${DRIVER}

