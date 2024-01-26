"""prompts to be used"""

from string import Template

DEFAULT_QUERY_PROMPT_TMPL = Template(
    """Context information is below.

----------
${context_str}
----------

Given the context information and not prior knowledge, answer the question: ${query_str}
"""
)