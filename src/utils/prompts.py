analyst_instructions="""
You are tasked with creating a set of AI analyst personas. 
Follow these instructions carefully:
1. First, review research topic:
{topic}
2. Examine any editorial feedback that has been optionally provided to guide creation of the analyst
{human_analyst_feedback}
3. Determine the most interesting theme based upon documents and / or feedback above.
4. Pick the top {max_analysts} themes.
5. Assigned one analyst to each theme.

"""