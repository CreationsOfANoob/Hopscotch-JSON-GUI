def getRules(fileDictionary):
    return fileDictionary["rules"]

def getObjects(fileDictionary):
    return fileDictionary["objects"]

def getAbilities(fileDictionary):
    return fileDictionary["abilities"]

def getVariables(fileDictionary):
    return fileDictionary["variables"]


def getAbilityWithID(ID,fileDictionary):
    for ability in fileDictionary["abilities"]:
        if ability["abilityID"] == ID:
            return ability

def getVariableWithID(ID,fileDictionary):
    for variable in fileDictionary["variables"]:
        if variable["objectIdString"] == ID:
            return variable


def getWhenWithID(ID,fileDictionary):
    for rule in fileDictionary["rules"]:
        if rule["id"] == ID:
            return rule


def getRulesOfObject(HSobject,fileDictionary):
    rules = []
    IDs = HSobject["rules"]
    for rule in fileDictionary["rules"]:
        if rule["id"] in IDs:
            rules.append(rule)
    return rules

def getStrOfDatum(datum,filedictionary):
    if datum.get("params",0) != 0:
        if len(datum["params"]) == 1:
            strToReturn = getStrOfParam(datum["params"][0],filedictionary)# + " " + datum["description"]
        else:
            strToReturn = getStrOfParam(datum["params"][0],filedictionary) + " " + datum["description"] + getStrOfParam(datum["params"][1],filedictionary)
    else:
        if datum.get("variable",0) == 0:
            strToReturn = datum["description"]
        else:
            strToReturn = getVariableWithID(datum["variable"],filedictionary)["name"]
    return strToReturn

def getStrOfParam(param,filedictionary):
    if param.get("datum",0) != 0:
        return "(" + getStrOfDatum(param["datum"],filedictionary) + ")"
    else:
        return param["value"]


def getStrEventOfWhen(HSrule,filedictionary):
    result = ""
    if HSrule["parameters"][0]["datum"]["block_class"] == "conditionalOperator":
        result = result + getStrOfParam(HSrule["parameters"][0]["datum"]["params"][0],filedictionary)
        result = result + HSrule["parameters"][0]["datum"]["description"]
        result = result + HSrule["parameters"][0]["datum"]["params"][1]["value"]
    else:
        result = HSrule["parameters"][0]["datum"]["description"]
    return result


def abilityExists(ID,fileDictionary):
    for i in fileDictionary["abilities"]:
        if i["abilityID"] == ID:
            return True
    return False

def remove_emoji(stringToFix):
    import re
    emoji_pattern = re.compile("["
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                           "]+", flags=re.UNICODE)
    return (emoji_pattern.sub(r'', stringToFix)) # no emoji
