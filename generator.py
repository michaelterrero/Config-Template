from jinja2 import Environment, FileSystemLoader
import yaml

#Load data from YAML file into Python dictionary
config = yaml.full_load(open('./var.yaml'))

#Load Jinja2 template
env = Environment(loader = FileSystemLoader('./'), trim_blocks=True, lstrip_blocks=True)
template = env.get_template('./Router/IOS-XE/Ciscorouter.j2')

#Render template using data and print the output
print(template.render(config))

#Save configuration to txt file. 
#Currently working to dynaically name the txt file with var.yaml "HOST" variable
with open('hostname.txt', 'w') as configfile:
   configfile.write(template.render(config))
