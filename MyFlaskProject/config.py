from ibm_watsonx_ai.metanames import GenTextParamsMetaNames as GenParams

API_KEY = ""
PROJECT_ID = ""
URL = "https://eu-de.ml.cloud.ibm.com"

# Model IDs
LLAMA_MODEL_ID = "meta-llama/llama-3-3-70b-instruct"
GRANITE_MODEL_ID = "ibm/granite-4-h-small"
MISTRAL_MODEL_ID = "mistralai/mistral-small-3-1-24b-instruct-2503"

CREDENTIALS = {
    "url": URL,
    "api_key" : API_KEY
}

PARAMETERS = {
    GenParams.DECODING_METHOD: "greedy",
    GenParams.MAX_NEW_TOKENS: 256,
}

