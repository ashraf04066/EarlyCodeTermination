#!/bin/bash


# Project 1
cd /home/ashraf/projects/flacoco-1.0.2/flacoco-1.0.2/examples/lang_1_buggy_collector
mvn clean
mvn -Dtest=NumberUtilsTest#TestLang747 test 
mvn jacoco:report


# Project 4
cd /home/ashraf/projects/flacoco-1.0.2/flacoco-1.0.2/examples/lang_4_buggy_collector
mvn clean
mvn -Dtest=LookupTranslatorTest#testLang882 test
mvn jacoco:report

# Project 5
cd /home/ashraf/projects/flacoco-1.0.2/flacoco-1.0.2/examples/lang_5_buggy_collector
mvn clean
mvn -Dtest=LocaleUtilsTest#testLang865 test
mvn jacoco:report

# Project 6
cd /home/ashraf/projects/flacoco-1.0.2/flacoco-1.0.2/examples/lang_6_buggy_collector
mvn clean
mvn -Dtest=StringUtilsTest#testEscapeSurrogatePairs test
mvn jacoco:report


# Project 11
cd /home/ashraf/projects/flacoco-1.0.2/flacoco-1.0.2/examples/lang_11_buggy_collector
mvn clean
mvn -Dtest=RandomStringUtilsTest#testLANG807 test 
mvn jacoco:report


# Project 14
cd /home/ashraf/projects/flacoco-1.0.2/flacoco-1.0.2/examples/lang_14_buggy_collector
mvn clean
mvn -Dtest=StringUtilsEqualsIndexOfTest#testEquals test
mvn jacoco:report

# Project 18
cd /home/ashraf/projects/flacoco-1.0.2/flacoco-1.0.2/examples/lang_18_buggy_collector
mvn clean
mvn -Dtest=FastDateFormatTest#testShortDateStyleWithLocales test
mvn jacoco:report

# Project 19
cd /home/ashraf/projects/flacoco-1.0.2/flacoco-1.0.2/examples/lang_19_buggy_collector
mvn clean
mvn -Dtest=NumericEntityUnescaperTest#testOutOfBounds test
mvn jacoco:report


# Project 20
cd /home/ashraf/projects/flacoco-1.0.2/flacoco-1.0.2/examples/lang_20_buggy_collector
mvn clean
mvn -Dtest=StringUtilsTest#testJoin_Objectarray,StringUtilsTest#testJoin_ArrayChar test
mvn jacoco:report

# Project 21
cd /home/ashraf/projects/flacoco-1.0.2/flacoco-1.0.2/examples/lang_21_buggy_collector
mvn clean
mvn -Dtest=DateUtilsTest#testIsSameLocalTime_Cal test
mvn jacoco:report

# Project 22
cd /home/ashraf/projects/flacoco-1.0.2/flacoco-1.0.2/examples/lang_22_buggy_collector
mvn clean
mvn -Dtest=FractionTest#testReduce,FractionTest#testReducedFactory_int_int test
mvn jacoco:report

# Project 23
cd /home/ashraf/projects/flacoco-1.0.2/flacoco-1.0.2/examples/lang_23_buggy_collector
mvn clean
mvn -Dtest=ExtendedMessageFormatTest#testEqualsHashcode test
mvn jacoco:report


# Project 29
cd /home/ashraf/projects/flacoco-1.0.2/flacoco-1.0.2/examples/lang_29_buggy_collector
mvn clean
mvn -Dtest=SystemUtilsTest#testJavaVersionAsInt test
mvn jacoco:report

# Project 30
cd /home/ashraf/projects/flacoco-1.0.2/flacoco-1.0.2/examples/lang_30_buggy_collector
mvn clean
mvn -Dtest=StringUtilsEqualsIndexOfTest#testContainsAny_StringCharArrayWithBadSupplementaryChars,StringUtilsEqualsIndexOfTest#testContainsAny_StringWithBadSupplementaryChars,StringUtilsEqualsIndexOfTest#testContainsNone_CharArrayWithBadSupplementaryChars,StringUtilsEqualsIndexOfTest#testContainsNone_CharArrayWithSupplementaryChars,StringUtilsEqualsIndexOfTest#testContainsNone_StringWithBadSupplementaryChars,StringUtilsEqualsIndexOfTest#testContainsNone_StringWithSupplementaryChars,StringUtilsEqualsIndexOfTest#testIndexOfAny_StringCharArrayWithSupplementaryChars,StringUtilsEqualsIndexOfTest#testIndexOfAny_StringStringWithSupplementaryChars,StringUtilsEqualsIndexOfTest#testIndexOfAnyBut_StringCharArrayWithSupplementaryChars,StringUtilsEqualsIndexOfTest#testIndexOfAnyBut_StringStringWithSupplementaryChars test
mvn jacoco:report

# Project 31
cd /home/ashraf/projects/flacoco-1.0.2/flacoco-1.0.2/examples/lang_31_buggy_collector
mvn clean
mvn -Dtest=StringUtilsEqualsIndexOfTest#testContainsAnyStringWithSupplementaryChars,StringUtilsEqualsIndexOfTest#testContainsAnyCharArrayWithSupplementaryChars test
mvn jacoco:report

# Project 32
cd /home/ashraf/projects/flacoco-1.0.2/flacoco-1.0.2/examples/lang_32_buggy_collector
mvn clean
mvn -Dtest=HashCodeBuilderTest#testReflectionObjectCycle test
mvn jacoco:report

# Project 40
cd /home/ashraf/projects/flacoco-1.0.2/flacoco-1.0.2/examples/lang_40_buggy_collector
mvn clean
mvn -Dtest=StringUtilsEqualsIndexOfTest#testContainsIgnoreCase_LocaleIndependence test
mvn jacoco:report

# Project 41
cd /home/ashraf/projects/flacoco-1.0.2/flacoco-1.0.2/examples/lang_41_buggy_collector
mvn clean
mvn -Dtest=ClassUtilsTest#test_getPackageName_Class,ClassUtilsTest#test_getShortClassName_Class test
mvn jacoco:report