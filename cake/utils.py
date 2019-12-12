import collections

from cerberus import Validator
from django.http import JsonResponse


def get_smallest_repeating_segment(sequence):
    sequence_size = len(sequence)
    max_rotations = sequence_size // 2

    original_sequence = collections.deque(sequence)
    next_sequence = collections.deque(sequence)
    rotations = 1
    next_sequence.rotate(1)
    while next_sequence != original_sequence and rotations <= max_rotations:
        rotations += 1
        next_sequence.rotate(1)

    if next_sequence != original_sequence:
        smallest_repeating_segment = sequence
        smallest_repeating_segment_size = sequence_size
        repetitions = 1
    else:
        smallest_repeating_segment = ''.join(next_sequence)[:rotations]
        smallest_repeating_segment_size = rotations
        repetitions = sequence_size // rotations

    return smallest_repeating_segment, smallest_repeating_segment_size, repetitions


def validate_cake_pattern(data):
    schema = {
        'cake': {'type': 'string', 'empty': False, 'maxlength': 200},
    }
    validator = Validator(require_all=True)
    validator.validate(data, schema)
    return validator


def compose_response(status, data=None, message=None):
    response = {
        'status': 'success' if status == 200 else 'error'
    }
    if data:
        response['data'] = data
    if message:
        response['message'] = message
    print(response)
    return JsonResponse(response, status=status)
