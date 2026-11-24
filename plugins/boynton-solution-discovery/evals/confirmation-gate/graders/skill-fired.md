---
type: tool_used
tool: Skill
input_match: '"skill"\s*:\s*"(?:[\w-]+:)?solution-discovery"'
min: 1
weight: 1
---

Indicator: the `solution-discovery` skill should be invoked for this case. Under a with/without
ablation this is a plugin-fired indicator, not part of the base score.
