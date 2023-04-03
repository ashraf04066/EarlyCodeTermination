#!/bin/bash


# Project 8
cd /home/ashraf/projects/flacoco-1.0.2/flacoco-1.0.2/examples/time_10_buggy
mvn clean
mvn -Dtest=TestDays#testFactory_daysBetween_RPartial_MonthDay,TestMonths#testFactory_monthsBetween_RPartial_MonthDay test 
mvn jacoco:report


# Project 10
cd /home/ashraf/projects/flacoco-1.0.2/flacoco-1.0.2/examples/time_8_buggy
mvn clean
mvn -Dtest=LookupTranslatorTest#testForOffsetHoursMinutes_int_int test
mvn jacoco:report

# Project 5
cd /home/ashraf/projects/flacoco-1.0.2/flacoco-1.0.2/examples/time_19_buggy
mvn clean
mvn -Dtest=TestDateTimeZoneCutover#testDateTimeCreation_london test
mvn jacoco:report

# Project 6
cd /home/ashraf/projects/flacoco-1.0.2/flacoco-1.0.2/examples/time_22_buggy
mvn clean
mvn -Dtest=TestDuration_Basics#testToPeriod_fixedZone,TestPeriod_Constructors#testConstructor_long_fixedZone test
mvn jacoco:report


# Project 6
cd /home/ashraf/projects/flacoco-1.0.2/flacoco-1.0.2/examples/time_26_buggy
mvn clean
mvn -Dtest=TestDateTimeZoneCutover#testBug2182444_usCentral,TestDateTimeZoneCutover#testBug2182444_ausNSW,TestDateTimeZoneCutover#testWithMinuteOfHourInDstChange_mockZone test
mvn jacoco:report