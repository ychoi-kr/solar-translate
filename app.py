from openai import OpenAI
import streamlit as st


def update_last_content():
    st.session_state.messages[-1]["content"] = st.session_state.new_content


def count_lines(text):
    return text.count("\n") + 1


st.title("Solar Custom Translate")
st.write(
    """ Translate between English and Korean using Solar Mini. 
    You can customize the translation style by editing the translation result.
    """
)
st.write("Visit https://console.upstage.ai to get your Solar API key.")

models = {
    "enko": "upstage/solar-1-mini-translate-enko",
    "koen": "upstage/solar-1-mini-translate-koen",
}

client = OpenAI(
    api_key=st.secrets["SOLAR_API_KEY"], base_url="https://api.upstage.ai/v1/solar"
)


if "model_name" not in st.session_state:
    st.session_state["model_name"] = models["enko"]

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


if prompt := st.chat_input("Text to translate"):
    with st.chat_message("user"):
        if prompt.startswith("@"):
            model_tag = prompt[1:].split()[0]
            if model_tag in models:
                st.session_state["model_name"] = models[model_tag]
                st.markdown(f"**Switched to `{st.session_state['model_name']}`**")
                prompt = prompt.replace(f"@{model_tag}", "").strip()
        st.markdown(prompt)

    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("assistant"):
        stream = client.chat.completions.create(
            model=st.session_state["model_name"],
            messages=[
                {"role": m["role"], "content": m["content"]}
                for m in st.session_state.messages
            ],
            stream=True,
        )
        output_area = st.empty()
        response = output_area.write_stream(stream)
        response = output_area.text_area(
            label="",
            value=response,
            on_change=update_last_content,
            height=count_lines(response) * 20 + 20,
            key="new_content",
        )
    st.session_state.messages.append({"role": "assistant", "content": response})


col1, col2 = st.columns(2)
with col1:
    on = st.toggle(label="translation mode", value=True)
    if on:
        st.session_state["model_name"] = models["enko"]
        tranlate_mode = "EN → KO"
    else:
        st.session_state["model_name"] = models["koen"]
        tranlate_mode = "KO → EN"
with col2:
    st.write(tranlate_mode)

if st.session_state.messages and st.button("Start over"):
    st.session_state.messages = []
    # refresh the page
    st.rerun()
