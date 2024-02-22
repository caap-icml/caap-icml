import os
from src.utils.file import read_text_file


PROJECT_LIST = []

env_list_path = "./data/env_list.txt"
env_list = read_text_file(env_list_path).split('\n')

seed_list = list(range(0,100))
# In the case of click_menu_2, there were some cases where instructions were given in the form of a icon instead of natural language.
seed_list_for_click_menu_2 = [0,1,5,8,9,10,11,13,15,16,17,22,24,26,29,33,34,35,40,41,43,44,45,46,47,
48,49,50,52,53,57,58,59,60,64,67,68,70,75,77,78,79,80,81,82,83,84,86,88,89,
91,93,94,95,98,100,101,102,105,106,109,113,115,116,117,119,122,124,126,127,128,130,133,135,137,
140,142,143,144,147,148,150,151,153,156,157,161,163,165,169,171,172,174,175,176,177,178,179,188,189]


scripts_path = "./data/human_demo_scripts"
script_list = [script for script in os.listdir(scripts_path) if script.endswith('.txt')]

start_idx = 0
batch_size = 100

## PROJECT 1
project = {}
# Set GPT version
project['GPT_version'] = '4'
# Set commentator name
project['VISUALOBSERVER_COMMENTATOR'] = 'commentator_v01'
# Set prompt ['None' , 'all', 'part1', 'part2', 'part3', 'part4']
project['exclude_prompt_type'] = 'None'

project['name']= f"Exclude_{project['exclude_prompt_type']}__GPT_{project['GPT_version']}__seed_{start_idx}_{start_idx+batch_size-1}"

project['JOB_CONFIG_LIST'] = []
JOB_CONFIG_LIST = []

need_act_from_the_top_env_list = ['choose-list',]

for idx in range(start_idx,start_idx+batch_size):
    for task_name in env_list:
        job_config = {}
        job_config['task'] = task_name
        job_config['seed_list'] = [seed_list[idx]]
        job_config['max_action_cnt'] = 25
        if task_name in ['guess-number']:
            job_config['max_action_cnt'] = 50
        if task_name == 'click-menu-2':
            job_config['seed_list'] = [seed_list_for_click_menu_2[idx]]

        if task_name in need_act_from_the_top_env_list:
            job_config['act_from_the_top'] = True
        job_config['demo_script_file_list'] = [os.path.join(scripts_path, script) for script in script_list if script.startswith(task_name.replace('-', '_')+'_3')]
        JOB_CONFIG_LIST.append(job_config)
project['JOB_CONFIG_LIST'] = JOB_CONFIG_LIST
PROJECT_LIST.append(project)