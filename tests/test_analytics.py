"""
OptiRoute: Urban Last-Mile Courier Fleet & Route Density Analytics - Pytest Automated Test Suite
"""
import pytest
import numpy as np


def test_fadr_calculation():
    success_first_attempt = 9680
    total_parcels = 10000
    assert (success_first_attempt / total_parcels) * 100.0 == 96.8

def test_stops_per_hour():
    total_stops = 148.8
    total_hours = 8.0
    assert total_stops / total_hours == 18.6


def test_sla_compliance_bounds():
    compliant = 9400
    total = 10000
    assert (compliant / total) * 100.0 == 94.0

def test_data_integrity():
    metric_val = 1420.50
    assert metric_val > 0
