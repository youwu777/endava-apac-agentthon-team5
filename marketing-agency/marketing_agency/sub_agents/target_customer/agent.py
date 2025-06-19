# Copyright 2025 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""target_customer_agent: for identifying target audiences and customer personas"""

from google.adk import Agent
from google.adk.tools import google_search

from . import prompt

MODEL = "gemini-2.0-flash-001" 

target_customer_agent = Agent(
    model=MODEL,
    name="target_customer_agent",
    instruction=prompt.TARGET_CUSTOMER_PROMPT,
    output_key="target_customer_output",
    tools=[google_search],
) 