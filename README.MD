Unit test 
    -should not use filesystem, database, network(i.e should be all in memory)

Each test case should have 3 parts
1) Arrange -> Can have multiple
2) Act -> should only have 1
3) Assert -> should only have 1

Purpose
1) Understand what you want to build - Thinks through details
2) Decompose to loosely coupled units
3) Design interface and implementation separately (Think newspaper headline and body)
4) Regression

Limitations
1) Hard to write if many dependencies(poor design)
2) Test may be different from prod behaviour
3) Unit tests does not cover integration

When?
Approaches:
    1) Test Last
        + No need to invest time up front to think about test
        - Might create design that is untestable
    2) Test First
        + Thinks through details before starting to code
        - Might take longer to get to working code
Together with code. TDD suggest writing iterative approach 

Mocking
See telemetry.py and test_telemetry.py on how TelemetryClient is mocked to prevent network calls