"""
Unit 1 Lab
The student file must be named unit1_lab_bronze.py, unit1_lab_silver.py or
unit1_lab_gold.py. The tier is read from the file name.

SCORING
-------
There are 20 tests, worth 0.5 marks each (10 marks total).
  * 14 BRONZE tests - run for every tier
  *  3 SILVER tests - run for silver and gold, SKIPPED for bronze
  *  3 GOLD tests   - run for gold only, SKIPPED for bronze and silver

A skipped test earns no marks, so the maximum grade is capped by the tier:
  bronze = 14/20 = 7/10     silver = 17/20 = 8.5/10     gold = 20/20 = 10/10

GitHub Classroom: use the "Run command" / pytest grading test with
  pytest test_unit1_lab.py
or add one test per entry below (0.5 points each). Keep conftest.py beside
this file; it prints the final "GRADE: x/10" line.
"""

import builtins
import contextlib
import io
import os
import re
import runpy
import subprocess
import sys

import pytest

HERE = os.path.dirname(os.path.abspath(__file__))


def _find_student_file():
    for folder in (os.getcwd(), HERE):
        if not os.path.isdir(folder):
            continue
        for fname in sorted(os.listdir(folder)):
            if re.match(r"unit[01]_lab_(bronze|silver|gold)\.py$", fname, re.IGNORECASE):
                return os.path.join(folder, fname)
    return None


STUDENT_FILE = _find_student_file()
TIER = "bronze"
if STUDENT_FILE:
    TIER = re.search(r"(bronze|silver|gold)", os.path.basename(STUDENT_FILE), re.IGNORECASE).group(1).lower()

WELCOME = "Welcome to Goetz Haunted House!"
ADULT = "You can enter the 13+ haunted attraction."
FAMILY = "You can visit the family-friendly attractions."
SENIOR = "You qualify for a senior discount!"
CHILD = "You qualify for a child discount!"
REGULAR = "Regular ticket pricing applied."
JOIN = "Join our rewards program to save 10%!"
INVALID = "Invalid response. Join our rewards program to save 10%!"
GROUP = "You're eligible for our group after-dark haunted attraction package!"
STANDARD = "Standard ticket purchase - enjoy the haunted house!"


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def make_inputs(name="Sarah", age="15", tickets="2", member="no"):
    if TIER == "bronze":
        return [name, age]
    if TIER == "silver":
        return [name, age, tickets]
    return [name, age, tickets, member]


def require_file():
    if STUDENT_FILE is None:
        pytest.fail(
            "No student file found. Expected unit1_lab_bronze.py, "
            "unit1_lab_silver.py or unit1_lab_gold.py."
        )


def run_script(inputs):
    """Run the student script with the given stdin lines and return stdout."""
    require_file()
    result = subprocess.run(
        [sys.executable, STUDENT_FILE],
        input="\n".join(inputs) + "\n",
        capture_output=True,
        text=True,
        timeout=10,
    )
    assert result.returncode == 0, (
        f"Your program crashed:\n{result.stderr}\nOutput so far:\n{result.stdout}"
    )
    return result.stdout


def run_for_variables(inputs):
    """Run the script in-process and return (stdout, module globals)."""
    require_file()
    answers = iter(inputs)

    def fake_input(prompt=""):
        print(prompt, end="")
        return next(answers)

    buf = io.StringIO()
    real_input = builtins.input
    builtins.input = fake_input
    try:
        with contextlib.redirect_stdout(buf):
            try:
                names = runpy.run_path(STUDENT_FILE, run_name="__main__")
            except StopIteration:
                pytest.fail("Your program asked for more input than expected.")
    finally:
        builtins.input = real_input
    return buf.getvalue(), names


def lines_of(out):
    return [ln.strip() for ln in out.splitlines() if ln.strip()]


def money(out, amount):
    """True if the output contains $amount (e.g. 24 or 24.00)."""
    return re.search(r"\$\s*" + re.escape(amount) + r"(?!\d)", out) is not None


def skip_unless(min_tier):
    order = ["bronze", "silver", "gold"]
    if order.index(TIER) < order.index(min_tier):
        pytest.skip(f"{min_tier.title()} tier tests are not part of a {TIER.title()} submission.")


# ---------------------------------------------------------------------------
# BRONZE (14 tests, 7/10)
# ---------------------------------------------------------------------------

def test_b01_file_named_correctly():
    """Submitted file is named unit1_lab_<tier>.py."""
    require_file()
    assert os.path.isfile(STUDENT_FILE)


def test_b02_welcome_message():
    """Exact welcome message is printed first."""
    out = run_script(make_inputs())
    assert lines_of(out)[0].startswith(WELCOME), f"Expected '{WELCOME}' first.\nActual:\n{out}"


def test_b03_asks_for_name_and_age():
    """Program prompts with input() for name and age."""
    out = run_script(make_inputs())
    assert "name" in out.lower() and "old" in out.lower(), f"Prompts for name and age missing.\nActual:\n{out}"


def test_b04_greeting_output():
    """Personalised greeting matches the sample output."""
    out = run_script(make_inputs(name="Sarah", age="15"))
    assert "Hello Sarah, you are 15 years old." in out, f"Actual:\n{out}"


def test_b05_greeting_other_values():
    """Greeting uses the variables (different name and age)."""
    out = run_script(make_inputs(name="Marcus", age="19"))
    assert "Hello Marcus, you are 19 years old." in out, f"Actual:\n{out}"


def test_b06_name_variable_value():
    """A variable stores the name that was entered."""
    _, names = run_for_variables(make_inputs(name="Zelda", age="21"))
    assert "Zelda" in [v for v in names.values() if isinstance(v, str)], (
        "No variable holds the name entered ('Zelda')."
    )


def test_b07_age_variable_value():
    """A variable stores the age that was entered (as int or str)."""
    _, names = run_for_variables(make_inputs(name="Zelda", age="21"))
    assert any(v == 21 or v == "21" for v in names.values() if isinstance(v, (int, str))), (
        "No variable holds the age entered (21)."
    )


def test_b08_age_15_enters_13plus():
    """Age 15 sees the 13+ message and not the family message."""
    if TIER == "gold":
        return  # replaced by the gold conditional
    out = run_script(make_inputs(age="15"))
    assert ADULT in out and FAMILY not in out, f"Actual:\n{out}"


def test_b09_age_13_boundary():
    """Age exactly 13 is allowed into the 13+ attraction."""
    if TIER == "gold":
        return  # replaced by the gold conditional
    out = run_script(make_inputs(age="13"))
    assert ADULT in out and FAMILY not in out, f"Age 13 should enter 13+.\nActual:\n{out}"


def test_b10_age_12_family():
    """Age 12 sees the family-friendly message only."""
    if TIER == "gold":
        return  # replaced by the gold conditional
    out = run_script(make_inputs(age="12"))
    assert FAMILY in out and ADULT not in out, f"Actual:\n{out}"


def test_b11_age_5_family():
    """A young child sees the family-friendly message only."""
    if TIER == "gold":
        return  # replaced by the gold conditional
    out = run_script(make_inputs(age="5"))
    assert FAMILY in out and ADULT not in out, f"Actual:\n{out}"


def test_b12_age_70_enters_13plus():
    """An older visitor sees the 13+ message."""
    if TIER == "gold":
        return  # replaced by the gold conditional
    out = run_script(make_inputs(age="70"))
    assert ADULT in out, f"Actual:\n{out}"


def test_b13_output_order():
    """Welcome, then greeting appear in the correct order."""
    out = run_script(make_inputs(name="Sarah", age="15"))
    assert 0 <= out.find(WELCOME) < out.find("Hello Sarah"), f"Actual:\n{out}"


def test_b14_has_comments():
    """File has a header comment and several explanatory comments."""
    require_file()
    with open(STUDENT_FILE, encoding="utf-8") as f:
        comments = [ln for ln in f if ln.strip().startswith("#")]
    assert len(comments) >= 4, "Add a header comment with your name, IPO comments and explanations."


# ---------------------------------------------------------------------------
# SILVER (3 tests, 8.5/10 total)
# ---------------------------------------------------------------------------

def test_s01_total_cost():
    """2 tickets cost $24; 5 tickets cost $60."""
    skip_unless("silver")
    out = run_script(make_inputs(tickets="2"))
    assert money(out, "24") or money(out, "24.00"), f"Expected $24 for 2 tickets.\nActual:\n{out}"
    out = run_script(make_inputs(tickets="5"))
    assert money(out, "60") or money(out, "60.00"), (
        f"Expected $60 for 5 tickets.\nActual:\n{out}"
    )


def test_s02_senior_and_child_discount():
    """Age 65+ gets senior message; age 12 or under gets child message."""
    skip_unless("silver")
    out = run_script(make_inputs(age="70"))
    assert SENIOR in out and CHILD not in out and REGULAR not in out, f"Actual:\n{out}"
    out = run_script(make_inputs(age="12"))
    assert CHILD in out and SENIOR not in out and REGULAR not in out, f"Actual:\n{out}"


def test_s03_regular_and_boundaries():
    """Ages 13, 64, 30 are regular; 65 is senior."""
    skip_unless("silver")
    for age in ("13", "30", "64"):
        out = run_script(make_inputs(age=age))
        assert REGULAR in out and SENIOR not in out and CHILD not in out, f"Age {age}.\nActual:\n{out}"
    out = run_script(make_inputs(age="65"))
    assert SENIOR in out, f"Age 65 should be senior.\nActual:\n{out}"


# ---------------------------------------------------------------------------
# GOLD (3 tests, 10/10 total)
# ---------------------------------------------------------------------------

def test_g01_rewards_member_yes():
    """'yes' prints the 10% discounted total: 4 tickets -> $43.20."""
    skip_unless("gold")
    out = run_script(make_inputs(age="19", tickets="4", member="yes"))
    assert re.search(r"discounted total( cost)? is: \$43\.20", out), f"Actual:\n{out}"
    assert JOIN not in out, f"Members should not see the join message.\nActual:\n{out}"


def test_g02_rewards_member_no_and_invalid():
    """'no' and invalid answers print their messages and the full total."""
    skip_unless("gold")
    out = run_script(make_inputs(age="12", tickets="4", member="no"))
    assert JOIN in out and INVALID not in out, f"Actual:\n{out}"
    assert re.search(r"total( cost)? is: \$48(\.00)?(?!\d)", out), f"Actual:\n{out}"
    out = run_script(make_inputs(age="12", tickets="4", member="maybe"))
    assert INVALID in out and re.search(r"total( cost)? is: \$48(\.00)?(?!\d)", out), f"Actual:\n{out}"


def test_g03_group_package():
    """Age 17+ AND 3+ tickets gets the group package, otherwise standard."""
    skip_unless("gold")
    out = run_script(make_inputs(age="19", tickets="4", member="yes"))
    assert GROUP in out and STANDARD not in out, f"Actual:\n{out}"
    out = run_script(make_inputs(age="17", tickets="3", member="no"))
    assert GROUP in out, f"Age 17 with 3 tickets qualifies.\nActual:\n{out}"
    for age, tickets in (("16", "5"), ("30", "2")):
        out = run_script(make_inputs(age=age, tickets=tickets, member="no"))
        assert STANDARD in out and GROUP not in out, f"Age {age}, {tickets} tickets.\nActual:\n{out}"
