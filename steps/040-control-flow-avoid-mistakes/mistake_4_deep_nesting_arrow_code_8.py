# Hard to read and debug
if response["status"] == 200:
    if response["body"]:
        if response["body"]["confidence"] > 0.5:
            if response["body"]["confidence"] > 0.9:
                label = "very confident"
            else:
                label = "confident"
        else:
            label = "uncertain"
    else:
        label = "empty"
else:
    label = "error"
