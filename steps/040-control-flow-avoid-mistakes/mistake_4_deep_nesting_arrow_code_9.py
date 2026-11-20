if response["status"] != 200:
    return "error"
if not response["body"]:
    return "empty"

confidence = response["body"]["confidence"]
if confidence > 0.9:
    return "very confident"
if confidence > 0.5:
    return "confident"
return "uncertain"
