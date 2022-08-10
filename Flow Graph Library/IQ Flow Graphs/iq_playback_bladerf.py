#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Iq Playback Bladerf
# Generated: Mon Sep  6 11:46:17 2021
##################################################


from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from optparse import OptionParser
import osmosdr
import time


class iq_playback_bladerf(gr.top_block):

    def __init__(self):
        gr.top_block.__init__(self, "Iq Playback Bladerf")

        ##################################################
        # Variables
        ##################################################
        self.tx_gain = tx_gain = 30
        self.tx_frequency = tx_frequency = 2425.715
        self.tx_channel = tx_channel = "A:0"
        self.sample_rate = sample_rate = 4
        self.ip_address = ip_address = "192.168.40.2"
        self.filepath = filepath = ""

        ##################################################
        # Blocks
        ##################################################
        self.osmosdr_sink_0 = osmosdr.sink( args="numchan=" + str(1) + " " + 'bladerf=0' )
        self.osmosdr_sink_0.set_sample_rate(float(sample_rate)*1e6)
        self.osmosdr_sink_0.set_center_freq(tx_frequency*1e6, 0)
        self.osmosdr_sink_0.set_freq_corr(0, 0)
        self.osmosdr_sink_0.set_gain(10, 0)
        self.osmosdr_sink_0.set_if_gain(20, 0)
        self.osmosdr_sink_0.set_bb_gain(tx_gain, 0)
        self.osmosdr_sink_0.set_antenna('', 0)
        self.osmosdr_sink_0.set_bandwidth(0, 0)

        self.blocks_file_source_0 = blocks.file_source(gr.sizeof_gr_complex*1, filepath, True)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.blocks_file_source_0, 0), (self.osmosdr_sink_0, 0))

    def get_tx_gain(self):
        return self.tx_gain

    def set_tx_gain(self, tx_gain):
        self.tx_gain = tx_gain
        self.osmosdr_sink_0.set_bb_gain(self.tx_gain, 0)

    def get_tx_frequency(self):
        return self.tx_frequency

    def set_tx_frequency(self, tx_frequency):
        self.tx_frequency = tx_frequency
        self.osmosdr_sink_0.set_center_freq(self.tx_frequency*1e6, 0)

    def get_tx_channel(self):
        return self.tx_channel

    def set_tx_channel(self, tx_channel):
        self.tx_channel = tx_channel

    def get_sample_rate(self):
        return self.sample_rate

    def set_sample_rate(self, sample_rate):
        self.sample_rate = sample_rate
        self.osmosdr_sink_0.set_sample_rate(float(self.sample_rate)*1e6)

    def get_ip_address(self):
        return self.ip_address

    def set_ip_address(self, ip_address):
        self.ip_address = ip_address

    def get_filepath(self):
        return self.filepath

    def set_filepath(self, filepath):
        self.filepath = filepath
        self.blocks_file_source_0.open(self.filepath, True)


def main(top_block_cls=iq_playback_bladerf, options=None):

    tb = top_block_cls()
    tb.start()
    tb.wait()


if __name__ == '__main__':
    main()