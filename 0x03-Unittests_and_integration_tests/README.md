0x03. Unittests and Integration Tests
UnitTests
Back-end
Integration tests
 Weight: 1
 Project will start Jun 27, 2024 6:00 AM, must end by Jul 2, 2024 6:00 AM
 Checker was released at Jun 28, 2024 12:00 PM
 An auto review will be launched at the deadline


Unit testing is the process of testing that a particular function returns expected results for different set of inputs. A unit test is supposed to test standard inputs and corner cases. A unit test should only test the logic defined inside the tested function. Most calls to additional functions should be mocked, especially if they make network or database calls.

The goal of a unit test is to answer the question: if everything defined outside this function works as expected, does this function work as expected?

Integration tests aim to test a code path end-to-end. In general, only low level functions that make external calls such as HTTP requests, file I/O, database I/O, etc. are mocked.

Integration tests will test interactions between every part of your code.

Execute your tests with

$ python -m unittest path/to/test_file.py
Resources
Read or watch:

unittest — Unit testing framework
unittest.mock — mock object library
How to mock a readonly property with mock?
parameterized
Memoization