# Importing Python modules
from xml.etree import ElementTree

def generateXml (data, gender_predicted, age_predicted, open_predicted, agr_predicted, ext_predicted, neu_predicted, con_predicted, output_path):
    for i in range(len(data)):
        file = output_path + data.loc[i, 'userid'] + ".xml"
        tree = ElementTree.ElementTree()
        root = ElementTree.Element("user")
        root.set("id", str(data.loc[i, 'userid']))
        root.set("age_group", str(age_predicted[i]))
        root.set("gender", str(gender_predicted[i]))
        root.set("extrovert", str(round(ext_predicted[i], 2)))
        root.set("neurotic", str(round(neu_predicted[i], 2)))
        root.set("agreeable", str(round(agr_predicted[i], 2)))
        root.set("conscientious", str(round(con_predicted[i], 2)))
        root.set("open", str(round(open_predicted[i], 2)))
        tree._setroot(root)
        tree.write(file)