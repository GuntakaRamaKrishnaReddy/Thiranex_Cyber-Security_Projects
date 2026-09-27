import streamlit as st
from analyzer import analyze_password, generate_password


# ---------------------------------
# Page Configuration
# ---------------------------------

st.set_page_config(
    page_title="Password Strength Analyzer",
    page_icon="🔐",
    layout="centered"
)


# ---------------------------------
# Header
# ---------------------------------

st.title("🔐 Password Strength Analyzer")

st.write(
    "Analyze your password strength using length, "
    "complexity, common-password detection and "
    "predictable-pattern checks."
)

st.divider()


# ---------------------------------
# Password Analyzer
# ---------------------------------

st.subheader("🔍 Analyze Password")

password = st.text_input(
    "Enter your password",
    type="password",
    placeholder="Enter password..."
)


if st.button("Analyze Password", use_container_width=True):

    if not password:

        st.warning("Please enter a password.")

    else:

        result = analyze_password(password)

        st.subheader("📊 Analysis Result")

        # -----------------------------
        # Basic Information
        # -----------------------------

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric(
                "Length",
                result["length"]
            )

        with col2:
            st.metric(
                "Score",
                f"{result['score']}/8"
            )

        with col3:
            st.metric(
                "Strength",
                result["strength"]
            )

        st.divider()

        # -----------------------------
        # Strength Progress
        # -----------------------------

        st.subheader("💪 Strength Meter")

        progress = min(result["score"] / 8, 1.0)

        st.progress(progress)

        if result["strength"] == "Very Weak":

            st.error("🔴 Very Weak")

        elif result["strength"] == "Weak":

            st.error("🟠 Weak")

        elif result["strength"] == "Medium":

            st.warning("🟡 Medium")

        elif result["strength"] == "Strong":

            st.success("🟢 Strong")

        else:

            st.success("🟢 Very Strong")

        # -----------------------------
        # Security Checks
        # -----------------------------

        st.subheader("🛡️ Security Checks")

        col1, col2 = st.columns(2)

        with col1:

            if result["lowercase"]:
                st.success("✓ Lowercase letters")
            else:
                st.error("✗ Lowercase letters")

            if result["uppercase"]:
                st.success("✓ Uppercase letters")
            else:
                st.error("✗ Uppercase letters")

            if result["number"]:
                st.success("✓ Numbers")
            else:
                st.error("✗ Numbers")

        with col2:

            if result["special"]:
                st.success("✓ Special characters")
            else:
                st.error("✗ Special characters")

            if result["common"]:
                st.error("✗ Common password")
            else:
                st.success("✓ Not a common password")

            if result["repeated"]:
                st.error("✗ Repeated characters")
            else:
                st.success("✓ No repeated pattern")

        # -----------------------------
        # Suggestions
        # -----------------------------

        st.subheader("💡 Recommendations")

        if result["suggestions"]:

            for suggestion in result["suggestions"]:

                st.info(suggestion)

        else:

            st.success(
                "No major issues detected."
            )


st.divider()


# ---------------------------------
# Password Generator
# ---------------------------------

st.subheader("🎲 Secure Password Generator")

st.write(
    "Generate a strong random password using "
    "cryptographically secure randomness."
)


length = st.slider(
    "Password Length",
    min_value=8,
    max_value=32,
    value=16
)


if st.button(
    "Generate Strong Password",
    use_container_width=True
):

    generated_password = generate_password(length)

    st.success("Strong password generated!")

    st.code(
        generated_password,
        language=None
    )

    st.caption(
        "Tip: Store generated passwords in a trusted "
        "password manager instead of reusing them."
    )


# ---------------------------------
# Footer
# ---------------------------------

st.divider()

st.caption(
    "Password Strength Analyzer • Cyber Security Project"
)
