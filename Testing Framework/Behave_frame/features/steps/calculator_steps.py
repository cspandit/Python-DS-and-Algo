from behave import *


@given(u'two inputs numbers are {num1} and {num2}')
def step_impl(context, num1, num2):
    context.num1 = int(num1)
    context.num2 = int(num2)


@when(u'calculation is performed')
def step_impl(context):
    context.result = context.num1+context.num2


@then(u'calculation should match expected result {expected_value}')
def step_impl(context, expected_value):
    assert context.result == int(expected_value)
