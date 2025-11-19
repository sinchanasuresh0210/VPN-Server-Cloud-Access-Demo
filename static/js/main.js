document.addEventListener("DOMContentLoaded", () => {
    const yearSpan = document.getElementById("year");
    if (yearSpan) {
        yearSpan.textContent = new Date().getFullYear().toString();
    }

    const navToggle = document.getElementById("navToggle");
    const navMenu = document.getElementById("navMenu");
    if (navToggle && navMenu) {
        navToggle.addEventListener("click", () => {
            const isOpen = navMenu.style.display === "flex" || navMenu.style.display === "block";
            navMenu.style.display = isOpen ? "none" : "flex";
        });
    }

    const chatForm = document.getElementById("chatForm");
    const chatInput = document.getElementById("chatInput");
    const chatMessages = document.getElementById("chatMessages");

    function appendMessage(text, type) {
        if (!chatMessages) return;
        const div = document.createElement("div");
        div.className = `message ${type}`;
        div.textContent = text;
        chatMessages.appendChild(div);
        chatMessages.scrollTop = chatMessages.scrollHeight;
    }

    if (chatForm && chatInput && chatMessages) {
        chatForm.addEventListener("submit", async (e) => {
            e.preventDefault();
            const text = chatInput.value.trim();
            if (!text) return;

            appendMessage(text, "user");
            chatInput.value = "";

            try {
                const res = await fetch("/api/ai-assistant", {
                    method: "POST",
                    headers: { "Content-Type": "application/json" },
                    body: JSON.stringify({ message: text }),
                });

                if (!res.ok) {
                    throw new Error("Request failed");
                }

                const data = await res.json();
                appendMessage(data.reply || "(No response)", "ai");
            } catch (err) {
                appendMessage("Sorry, the AI assistant is not available right now.", "ai");
            }
        });

        appendMessage("Hi! I am the VPNCLOUD mobile assistant. Ask me anything about secure, free cloud VPN access.", "ai");
    }
});
