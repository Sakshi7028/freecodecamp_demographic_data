from demographic_data_analyzer import demographic_data_analysis
import unittest
from test_module import DemographicAnalyzerTest

if __name__ == "__main__":
    # Run the demographic analysis and print results
    results = demographic_data_analysis()
    for key, value in results.items():
        print(f"{key}: {value}")

    # Run unit tests
    unittest.main()
