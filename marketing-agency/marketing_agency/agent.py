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

"""Marketing_coordinator Agent assists in creating effective online content."""

from google.adk.agents import LlmAgent
from google.adk.tools.agent_tool import AgentTool

from . import prompt
from .sub_agents.product_name_create import product_name_create_agent
from .sub_agents.target_customer import target_customer_agent
from .sub_agents.benefit_research import benefit_research_agent
from .sub_agents.feature import feature_agent
from .sub_agents.design import design_agent
from .sub_agents.competitor import competitor_agent
from .sub_agents.pricing_research import pricing_research_agent
from .sub_agents.cost_research import cost_research_agent
from .sub_agents.channel_sales import channel_sales_agent
from .sub_agents.marketing_content import marketing_content_agent

MODEL = "gemini-2.0-flash-001" 

marketing_coordinator = LlmAgent(
    name="marketing_coordinator",
    model=MODEL,
    description=(
        "Establish a powerful online presence and connect with your audience "
        "effectively. Guide you through defining your digital identity by"
        "choosing the perfect product name, identifying target customers, "
        "researching benefits, defining features, creating designs, analyzing "
        "competitors, developing pricing strategies, estimating costs, "
        "planning sales channels, and creating marketing content."
    ),
    instruction=prompt.MARKETING_COORDINATOR_PROMPT,
    tools=[
        AgentTool(agent=product_name_create_agent),
        AgentTool(agent=target_customer_agent),
        AgentTool(agent=benefit_research_agent),
        AgentTool(agent=feature_agent),
        AgentTool(agent=design_agent),
        AgentTool(agent=competitor_agent),
        AgentTool(agent=pricing_research_agent),
        AgentTool(agent=cost_research_agent),
        AgentTool(agent=channel_sales_agent),
        AgentTool(agent=marketing_content_agent),
    ],
)

root_agent = marketing_coordinator
