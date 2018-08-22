# anago-json-output
A small engine to give json output from Hironsan's Anago Bidirectional LSTM-CRF

This code is created for making Hironsan's Anago output to JSON format, so everyone using it on production can easily catch the ease of using standard JSON format.

Anago: https://github.com/Hironsan/anago

# The output command in anago:
text = 'President Obama is speaking at the White House.'
model.analyze(text)

# Output:
{
    "words": [
        "President",
        "Obama",
        "is",
        "speaking",
        "at",
        "the",
        "White",
        "House."
    ],
    "entities": [
        {
            "beginOffset": 1,
            "endOffset": 2,
            "score": 1,
            "text": "Obama",
            "type": "PER"
        },
        {
            "beginOffset": 6,
            "endOffset": 8,
            "score": 1,
            "text": "White House.",
            "type": "LOC"
        }
    ]
}

# With aviezab's Anago-JSON-Output:
text = 'President Obama is speaking at the White House.'
print (jsonkansaja (text))

{"Person": ["Obama"], "PoliticalOrg": [], "Facility": [], "Company": [], "GeopoliticalEnt": [], "Location": ["White House"], "Product": [], "Event": [], "WoArt": [], "Law": [], "Language": [], "Date": [], "Time": [], "Percentage": [], "Money": [], "Quantity": [], "Ordinal": [], "Cardinal": [], "Religion": []}

