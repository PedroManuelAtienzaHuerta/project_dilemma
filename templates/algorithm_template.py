"""
Copyright 2023-2025 Gabriele Ron

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""
from collections.abc import Sequence
from typing import Self

from project_dilemma.interfaces import Algorithm, Rounds


class AlgorithmTemplate(Algorithm):
    algorithm_id = 'algorithm_template'

    def __init__(self, mutations: Sequence[Self]):
        super().__init__(mutations)

    @staticmethod
    def decide(rounds: Rounds, **kwargs) -> bool:
        # Place algorithm here
        # Return true for cooperation, and false for defection
        raise NotImplementedError


# Set mutations here to avoid circular imports
AlgorithmTemplate.mutations = []
