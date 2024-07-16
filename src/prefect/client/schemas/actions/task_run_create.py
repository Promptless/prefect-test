from typing import Dict, List, Optional, Union
from uuid import UUID

from pydantic import Field

import prefect.client.schemas.objects as objects
from prefect._internal.schemas.bases import ActionBaseModel

from .state_create import StateCreate


class TaskRunCreate(ActionBaseModel):
    """Data used by the Prefect REST API to create a task run"""

    id: Optional[UUID] = Field(None, description="The ID to assign to the task run")
    # TaskRunCreate states must be provided as StateCreate objects
    state: Optional[StateCreate] = Field(
        default=None, description="The state of the task run to create"
    )

    name: Optional[str] = Field(
        default=None,
        description="The name of the task run",
    )
    flow_run_id: Optional[UUID] = Field(None)
    task_key: str = Field(
        default=..., description="A unique identifier for the task being run."
    )
    dynamic_key: str = Field(
        default=...,
        description=(
            "A dynamic key used to differentiate between multiple runs of the same task"
            " within the same flow run."
        ),
    )
    cache_key: Optional[str] = Field(None)
    cache_expiration: Optional[objects.DateTime] = Field(None)
    task_version: Optional[str] = Field(None)
    empirical_policy: objects.TaskRunPolicy = Field(
        default_factory=objects.TaskRunPolicy,
    )
    tags: List[str] = Field(default_factory=list)
    task_inputs: Dict[
        str,
        List[
            Union[
                objects.TaskRunResult,
                objects.Parameter,
                objects.Constant,
            ]
        ],
    ] = Field(default_factory=dict)