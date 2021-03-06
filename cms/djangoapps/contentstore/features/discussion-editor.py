# disable missing docstring
# pylint: disable=C0111

from lettuce import world, step


@step('I have created a Discussion Tag$')
def i_created_discussion_tag(step):
    world.create_course_with_unit()
    world.create_component_instance(
        step=step,
        category='discussion',
    )


@step('I see three alphabetized settings and their expected values$')
def i_see_only_the_settings_and_values(step):
    world.verify_all_setting_entries(
        [
            ['Category', "Week 1", False],
            ['Display Name', "Discussion", False],
            ['Subcategory', "Topic-Level Student-Visible Label", False]
        ])


@step('I edit the component$')
def i_edit_and_select_settings(_step):
    world.edit_component()
