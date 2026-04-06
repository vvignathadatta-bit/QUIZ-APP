import streamlit as st
import random

# ---------- QUESTIONS ----------
questions_data = [
    {"q": "Binary search complexity?", "options": ["O(n)", "O(log n)", "O(n log n)", "O(1)"], "ans": "O(log n)"},
    {"q": "FIFO structure?", "options": ["Stack", "Queue", "Tree", "Graph"], "ans": "Queue"},
    {"q": "DFS uses?", "options": ["Queue", "Stack", "Heap", "Tree"], "ans": "Stack"},
    {"q": "Best quicksort?", "options": ["O(n)", "O(n log n)", "O(n^2)", "O(log n)"], "ans": "O(n log n)"},
    {"q": "Worst quicksort?", "options": ["O(n log n)", "O(n^2)", "O(n)", "O(log n)"], "ans": "O(n^2)"},
    {"q": "LIFO structure?", "options": ["Queue", "Stack", "Tree", "Graph"], "ans": "Stack"},
    {"q": "Heap is?", "options": ["Sorted", "Binary tree", "Complete binary tree", "Graph"], "ans": "Complete binary tree"},
    {"q": "Merge sort?", "options": ["O(n^2)", "O(n log n)", "O(n)", "O(log n)"], "ans": "O(n log n)"},
    {"q": "Binary tree children?", "options": ["1", "2", "3", "4"], "ans": "2"},
    {"q": "Queue ops?", "options": ["Push", "Insert", "Enqueue/Dequeue", "Add"], "ans": "Enqueue/Dequeue"},
    {"q": "Stack ops?", "options": ["Enqueue", "Push/Pop", "Insert", "Delete"], "ans": "Push/Pop"},
    {"q": "Graph traversal?", "options": ["DFS/BFS", "Sort", "Search", "Insert"], "ans": "DFS/BFS"},
    {"q": "Linear search?", "options": ["O(n)", "O(log n)", "O(1)", "O(n log n)"], "ans": "O(n)"},
    {"q": "Hash avg?", "options": ["O(1)", "O(n)", "O(log n)", "O(n log n)"], "ans": "O(1)"},
    {"q": "Tree traversal?", "options": ["DFS", "BFS", "Inorder", "All"], "ans": "All"},
    {"q": "Recursion uses?", "options": ["Stack", "Queue", "Array", "Graph"], "ans": "Stack"},
    {"q": "Linked list access?", "options": ["O(1)", "O(n)", "O(log n)", "O(n log n)"], "ans": "O(n)"},
    {"q": "Binary search needs?", "options": ["Sorted", "Random", "Tree", "Graph"], "ans": "Sorted"},
    {"q": "AVL tree?", "options": ["Balanced", "Unbalanced", "Heap", "Graph"], "ans": "Balanced"},
    {"q": "Priority queue?", "options": ["Heap", "Stack", "Queue", "Tree"], "ans": "Heap"},
    {"q": "Insertion best?", "options": ["O(n)", "O(n^2)", "O(log n)", "O(n log n)"], "ans": "O(n)"},
    {"q": "Selection sort?", "options": ["Stable", "Unstable", "Fast", "Recursive"], "ans": "Unstable"},
    {"q": "Bubble worst?", "options": ["O(n)", "O(n log n)", "O(n^2)", "O(log n)"], "ans": "O(n^2)"},
    {"q": "Cycle detection?", "options": ["DFS", "Sort", "Search", "Insert"], "ans": "DFS"},
    {"q": "Dijkstra uses?", "options": ["Queue", "Stack", "Priority Queue", "Tree"], "ans": "Priority Queue"},
]

# ---------- SESSION ----------
if "quiz_started" not in st.session_state:
    st.session_state.quiz_started = False
    st.session_state.questions = []

# ---------- STYLING ----------
st.markdown("""
<style>
body {
    background: linear-gradient(135deg,#ff9a9e,#fad0c4);
}
.big-title {
    text-align:center;
    font-size:40px;
    font-weight:bold;
}
</style>
""", unsafe_allow_html=True)

# ---------- DASHBOARD ----------
if not st.session_state.quiz_started:
    st.markdown("<div class='big-title'>🎯 DSA Quiz App 💡</div>", unsafe_allow_html=True)
    st.write("### Test your skills & have fun 🚀")

    if st.button("Start Quiz 🚀"):
        st.session_state.quiz_started = True
        st.session_state.questions = random.sample(questions_data, 20)
        st.rerun()

# ---------- QUIZ ----------
else:
    st.header("💡 Quiz Time!")

    answers = []

    for i, q in enumerate(st.session_state.questions):
        choice = st.radio(
            f"{i+1}. {q['q']}",
            q["options"],
            index=None,  # ✅ No default selection
            key=i
        )
        answers.append(choice)

    # ---------- SUBMIT ----------
    if st.button("Submit ✅"):

        # ❗ Check all questions answered
        if None in answers:
            st.error("⚠️ Please answer all questions before submitting!")
        else:
            score = 0
            st.subheader("📊 Results")

            for i, q in enumerate(st.session_state.questions):
                if answers[i] == q["ans"]:
                    score += 1

                st.write(f"*Q{i+1}: {q['q']}*")
                st.write(f"Your answer: {answers[i]}")
                st.write(f"Correct answer: {q['ans']}")
                st.write("---")

            st.success(f"Your Score: {score} / 20")

            # 🎯 Result message
            if score == 20:
                st.success("🔥 Perfect Score!")
                st.balloons()
            elif score >= 15:
                st.success("🎉 Excellent!")
                st.balloons()
            elif score >= 10:
                st.warning("👍 Good Try!")
            else:
                st.error("😢 Keep Practicing!")

            # 🔄 Restart
            if st.button("Go Home 🏠"):
                st.session_state.quiz_started = False
                st.rerun()