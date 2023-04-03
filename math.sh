#!/bin/bash


# Project 2
cd /home/ashraf/projects/flacoco-1.0.2/flacoco-1.0.2/examples/math_original_2
mvn clean
mvn -Dtest=HypergeometricDistributionTest#testMath1021 test 
mvn jacoco:report


# Project 10
cd /home/ashraf/projects/flacoco-1.0.2/flacoco-1.0.2/examples/math_original_10
mvn clean
mvn -Dtest=DerivativeStructureTest#testAtan2SpecialCases test
mvn jacoco:report

# Project 15
cd /home/ashraf/projects/flacoco-1.0.2/flacoco-1.0.2/examples/math_original_15
mvn clean
mvn -Dtest=FastMathTest#testMath904 test
mvn jacoco:report

# Project 16
cd /home/ashraf/projects/flacoco-1.0.2/flacoco-1.0.2/examples/math_original_16
mvn clean
mvn -Dtest=FastMathTest#testMath905LargePositive,FastMathTest#testMath905LargeNegative test
mvn jacoco:report




# Project 33
cd /home/ashraf/projects/flacoco-1.0.2/flacoco-1.0.2/examples/math_original_33
mvn clean
mvn -Dtest=SimplexSolverTest#testMath781 test 
mvn jacoco:report


# Project 37
cd /home/ashraf/projects/flacoco-1.0.2/flacoco-1.0.2/examples/math_original_37
mvn clean
mvn -Dtest=ComplexTest#testTanhInf,ComplexTest#testTan,ComplexTest#testTanh,ComplexTest#testTanInf test
mvn jacoco:report

# Project 41
cd /home/ashraf/projects/flacoco-1.0.2/flacoco-1.0.2/examples/math_original_41
mvn clean
mvn -Dtest=VarianceTest#testEvaluateArraySegmentWeighted test
mvn jacoco:report

# Project 52
cd /home/ashraf/projects/flacoco-1.0.2/flacoco-1.0.2/examples/math_original_52
mvn clean
mvn -Dtest=RotationTest#testIssue639 test
mvn jacoco:report


# Project 53
cd /home/ashraf/projects/flacoco-1.0.2/flacoco-1.0.2/examples/math_original_53
mvn clean
mvn -Dtest=ComplexTest#testAddNaN test
mvn jacoco:report

# Project 54
cd /home/ashraf/projects/flacoco-1.0.2/flacoco-1.0.2/examples/math_original_54
mvn clean
mvn -Dtest=DfpTest#testIssue567 test
mvn jacoco:report

# Project 62
cd /home/ashraf/projects/flacoco-1.0.2/flacoco-1.0.2/examples/math_original_62
mvn clean
mvn -Dtest=MultiStartUnivariateRealOptimizerTest#testQuinticMin test
mvn jacoco:report

# Project 63
cd /home/ashraf/projects/flacoco-1.0.2/flacoco-1.0.2/examples/math_original_63
mvn clean
mvn -Dtest=GammaDistributionTest#testSampling,MathUtilsTest#testArrayEquals test
mvn jacoco:report


# Project 65
cd /home/ashraf/projects/flacoco-1.0.2/flacoco-1.0.2/examples/math_original_65
mvn clean
mvn -Dtest=LevenbergMarquardtOptimizerTest#testCircleFitting test
mvn jacoco:report

# Project 66
cd /home/ashraf/projects/flacoco-1.0.2/flacoco-1.0.2/examples/math_original_66
mvn clean
mvn -Dtest=MultiStartUnivariateRealOptimizerTest#testQuinticMin,MultiStartUnivariateRealOptimizerTest#testSinMin,BrentOptimizerTest#testQuinticMinStatistics,BrentOptimizerTest#testSinMin test
mvn jacoco:report

# Project 67
cd /home/ashraf/projects/flacoco-1.0.2/flacoco-1.0.2/examples/math_original_67
mvn clean
mvn -Dtest=MultiStartUnivariateRealOptimizerTest#testQuinticMin test
mvn jacoco:report

# Project 71
cd /home/ashraf/projects/flacoco-1.0.2/flacoco-1.0.2/examples/math_original_71
mvn clean
mvn -Dtest=ClassicalRungeKuttaIntegratorTest#testMissedEndEvent,DormandPrince853IntegratorTest#testMissedEndEvent test
mvn jacoco:report

# Project 72
cd /home/ashraf/projects/flacoco-1.0.2/flacoco-1.0.2/examples/math_original_72
mvn clean
mvn -Dtest=BrentSolverTest#testRootEndpoints test
mvn jacoco:report

# Project 75
cd /home/ashraf/projects/flacoco-1.0.2/flacoco-1.0.2/examples/math_original_75
mvn clean
mvn -Dtest=FrequencyTest#testPcts test
mvn jacoco:report

# Project 76
cd /home/ashraf/projects/flacoco-1.0.2/flacoco-1.0.2/examples/math_original_76
mvn clean
mvn -Dtest=SingularValueSolverTest#testMath320A,SingularValueSolverTest#testMath320B test
mvn jacoco:report

# Project 77
cd /home/ashraf/projects/flacoco-1.0.2/flacoco-1.0.2/examples/math_original_77
mvn clean
mvn -Dtest=ArrayRealVectorTest#testBasicFunctions,SparseRealVectorTest#testBasicFunctions test
mvn jacoco:report

# Project 80
cd /home/ashraf/projects/flacoco-1.0.2/flacoco-1.0.2/examples/math_original_80
mvn clean
mvn -Dtest=EigenDecompositionImplTest#testMathpbx02 test
mvn jacoco:report

# Project 84
cd /home/ashraf/projects/flacoco-1.0.2/flacoco-1.0.2/examples/math_original_84
mvn clean
mvn -Dtest=MultiDirectionalTest#testMinimizeMaximize,MultiDirectionalTest#testMath283 test
mvn jacoco:report

# Project 87
cd /home/ashraf/projects/flacoco-1.0.2/flacoco-1.0.2/examples/math_original_87
mvn clean
mvn -Dtest=SimplexSolverTest#testSingleVariableAndConstraint test
mvn jacoco:report

# Project 88
cd /home/ashraf/projects/flacoco-1.0.2/flacoco-1.0.2/examples/math_original_88
mvn clean
mvn -Dtest=SimplexSolverTest#testMath272 test
mvn jacoco:report


# Project 91
cd /home/ashraf/projects/flacoco-1.0.2/flacoco-1.0.2/examples/math_original_91
mvn clean
mvn -Dtest=FractionTest#testCompareTo test
mvn jacoco:report

# Project 92
cd /home/ashraf/projects/flacoco-1.0.2/flacoco-1.0.2/examples/math_original_92
mvn clean
mvn -Dtest=MathUtilsTest#testBinomialCoefficientLarge test
mvn jacoco:report

# Project 93
cd /home/ashraf/projects/flacoco-1.0.2/flacoco-1.0.2/examples/math_original_93
mvn clean
mvn -Dtest=MathUtilsTest#testFactorial test
mvn jacoco:report

# Project 102
cd /home/ashraf/projects/flacoco-1.0.2/flacoco-1.0.2/examples/math_original_102
mvn clean
mvn -Dtest=ChiSquareFactoryTest#testChiSquareLargeTestStatistic,ChiSquareFactoryTest#testChiSquare,ChiSquareTestTest#testChiSquareLargeTestStatistic,ChiSquareTestTest#testChiSquare,TestUtilsTest#testChiSquareLargeTestStatistic,TestUtilsTest#testChiSquare test
mvn jacoco:report

# Project 104
cd /home/ashraf/projects/flacoco-1.0.2/flacoco-1.0.2/examples/math_original_104
mvn clean
mvn -Dtest=GammaTest#testRegularizedGammaPositivePositive test
mvn jacoco:report