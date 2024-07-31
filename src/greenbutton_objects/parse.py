#!/usr/bin/python

import sys

from xsdata.formats.dataclass.context import XmlContext
from xsdata.formats.dataclass.parsers import XmlParser
from xsdata.formats.dataclass.parsers.config import ParserConfig

import greenbutton_objects.data.atom as atom
import greenbutton_objects.data.espi as espi
from greenbutton_objects import resources, utils


def parse_feed(filename):
    config = ParserConfig()
    context = XmlContext(class_type="pydantic")
    parser = XmlParser(context=context, config=config)

    data = parser.parse(filename, clazz=atom.Feed)

    usagePoints = [
        usage_point
        for entry in data.entry
        for content in entry.content
        for usage_point in content.content
        if isinstance(usage_point, espi.UsagePoint)
    ]

    meterReadings = []
    for entry in tree.getroot().findall("atom:entry/atom:content/espi:MeterReading/../..", utils.ns):
        mr = resources.MeterReading(entry, usagePoints=usagePoints)
        meterReadings.append(mr)

    readingTypes = []
    for entry in tree.getroot().findall("atom:entry/atom:content/espi:ReadingType/../..", utils.ns):
        rt = resources.ReadingType(entry, meterReadings=meterReadings)
        readingTypes.append(rt)

    intervalBlocks = []
    for entry in tree.getroot().findall("atom:entry/atom:content/espi:IntervalBlock/../..", utils.ns):
        ib = resources.IntervalBlock(entry, meterReadings=meterReadings)
        intervalBlocks.append(ib)

    return usagePoints


def parse_feed_representation(usage_points) -> str:
    """
    Return a string representation of the test_parse result.

    The representation includes the Usage Points, Meter Readings, and
    Interval Readings.
    """
    result = []
    for up in usage_points:
        result.append("UsagePoint (%s) %s %s:" % (up.title, up.serviceCategory.name, up.status))
        for mr in up.meterReadings:
            result.append("  Meter Reading (%s) %s:" % (mr.title, mr.readingType.uom.name))
            result.append("\n")
            for ir in mr.intervalReadings:
                result.append(
                    "    %s, %s: %s %s"
                    % (
                        ir.timePeriod.start,
                        ir.timePeriod.duration,
                        ir.value,
                        ir.value_symbol,
                    )
                )
                if ir.cost is not None:
                    result.append("(%s%s)" % (ir.cost_symbol, ir.cost))
                if len(ir.readingQualities) > 0:
                    result.append("[%s]" % ", ".join([rq.quality.name for rq in ir.readingQualities]))
                result.append("\n\n")
    return "".join(result)


if __name__ == "__main__":
    usage_points = parse_feed(sys.argv[1])
    representation = parse_feed_representation(usage_points)
    print(representation)
