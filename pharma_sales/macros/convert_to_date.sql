{% macro convert_to_date(date_string) %}
  {% set formats = [
    '%Y-%m-%d',
    '%d/%m/%Y',
    '%m/%d/%Y',
    '%Y%m%d',
    '%m-%d-%Y'
  ] %}

  {% set case_when_parts = [] %}

  {% for format in formats %}
    {% set format_expr = "STRPTIME(" ~ date_string ~ ", '" ~ format ~ "')" %}
    {% set case_when_part = "WHEN " ~ format_expr ~ " THEN " ~ format_expr %}
    {% set case_when_parts = case_when_parts + [case_when_part] %}
  {% endfor %}

  {% set final_sql = "CASE " ~ (case_when_parts | join(' ')) ~ " ELSE NULL END" %}

  -- Return the full CASE expression as a string
  {{ final_sql }}
{% endmacro %}
