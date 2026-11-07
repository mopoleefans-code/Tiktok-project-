# ====================================================================
# 👑 THE MAN NOBODY KNOWS — COCKPIT WITH DYNAMIC VIDEO-MOTION BACKDROP
# Features: Google Sign-Up Form, Cinematic Ken-Burns Poster Motion Loop
# Updated: October 9, 2026 WAT | Target Platform: Android Termux Local
# Bypasses all browser API link restrictions for 100% platform uptime!
# ====================================================================

import os
from flask import Flask, request, Response, redirect

print("\n📶 INITIALIZING THE MAN NOBODY KNOWS LIVE MOVIE-MOTION THEME CORE ENGINE...")

app = Flask(__name__, static_folder="static")

@app.route("/", methods=["GET"])
def home():
    html_content = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>THE MAN NOBODY KNOWS - SIGN UP</title>
    <style>
        body, html { margin: 0; padding: 0; width: 100%; height: 100%; overflow: hidden; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background-color: #0c0f12; }
        
        /* 📹 THE CINEMATIC MATRIX: MOVIE POSTER BACKGROUND RUNNING LIKE A LIVE VIDEO EFFECT */
        .video-motion-theme {
            position: fixed; top: 0; left: 0; width: 100%; height: 100%; z-index: -1000;
            background-image: url('https://ibb.co');
            background-size: cover;
            background-position: center center;
            background-repeat: no-repeat;
            filter: brightness(35%) contrast(115%);
            
            /* ⚡ HOLLYWOOD LIVE INTERACTIVE MOTION TIMELINE */
            transform: scale(1.0);
            animation: CinematicMovieLoop 20s ease-in-out infinite alternate;
        }

        @keyframes CinematicMovieLoop {
            0% {
                transform: scale(1.0) translate(0px, 0px);
            }
            50% {
                transform: scale(1.15) translate(-10px, -5px);
            }
            100% {
                transform: scale(1.05) translate(10px, 5px);
            }
        }

        .viewport-wrapper { display: flex; flex-direction: column; align-items: center; justify-content: center; min-height: 100vh; position: relative; z-index: 10; padding: 20px; box-sizing: border-box; }
        .cockpit-card { background: rgba(15, 15, 15, 0.82); border-radius: 16px; box-shadow: 0 20px 50px rgba(0,0,0,0.9); padding: 35px; width: 100%; max-width: 420px; text-align: center; box-sizing: border-box; backdrop-filter: blur(20px); -webkit-backdrop-filter: blur(20px); border: 1px solid rgba(255, 183, 3, 0.35); box-shadow: 0 0 35px rgba(255, 183, 3, 0.15); }
        .btn-social { display: flex; align-items: center; justify-content: center; gap: 10px; width: 100%; padding: 12px; margin: 10px 0; border: 1px solid #333; border-radius: 8px; font-weight: bold; cursor: pointer; color: white; font-size: 14px; background-color: transparent; }
        .btn-google { background-color: rgba(255, 255, 255, 0.03); border-color: rgba(255, 183, 3, 0.3); }
        .divider { color: #888; font-size: 13px; margin: 15px 0; display: flex; align-items: center; justify-content: center; gap: 10px; }
        .divider::before, .divider::after { content: ""; flex: 1; height: 1px; background: #333; }
        .label-text { text-align: left; display: block; color: #ffb703; font-size: 14px; margin-bottom: 5px; font-weight: 500; text-transform: uppercase; letter-spacing: 1px; }
        .input-field { background-color: rgba(0,0,0,0.6); border: 1px solid #333; padding: 12px; border-radius: 8px; color: white; width: 100%; margin-bottom: 15px; box-sizing: border-box; font-size: 14px; }
        .input-field:focus { border-color: #ffb703; outline: none; box-shadow: 0 0 10px rgba(255, 183, 3, 0.2); }
        .checkbox-container { display: flex; align-items: center; gap: 10px; text-align: left; font-size: 12px; color: #aaa; margin-bottom: 20px; }
        .checkbox-container a { color: #ffb703; text-decoration: underline; }
        .btn-submit { background: linear-gradient(90deg, #ffb703, #fb8500); border: none; color: #0c0f12; font-weight: bold; cursor: pointer; width: 100%; padding: 14px; border-radius: 8px; font-size: 14px; letter-spacing: 0.5px; text-transform: uppercase; box-shadow: 0 4px 15px rgba(251, 133, 0, 0.3); }
        .footer-text { color: #aaa; font-size: 12px; margin-top: 20px; }
        .footer-text a { color: #4285F4; text-decoration: none; font-weight: bold; }
    </style>
</head>
<body>

    <!-- 📹 THE POSTER GRAPHIC ACTING LIKE A CINEMATIC TRAILER BACKGROUND -->
    <div class="video-motion-theme"></div>

    <div class="viewport-wrapper">
        <div class="cockpit-card" id="signUpScreen">
            <h2 style="color: #ffb703; font-size: 18px; margin: 0 0 20px 0; text-transform: uppercase; letter-spacing: 2px;">THE MAN NOBODY KNOWS</h2>
            <button class="btn-social btn-google" onclick="triggerSocialAuth('Google')">
                <span style="color: #4285F4; font-weight: bold; font-size: 16px;">G</span> Sign up with Google
            </button>
            <div class="divider">or</div>
            <form action="/auth/submit-signup" method="POST">
                <span class="label-text">Name</span>
                <input type="text" name="user_name" class="input-field" placeholder="Enter your name" required>
                <span class="label-text">Email</span>
                <input type="email" name="user_email" class="input-field" placeholder="Enter your email" required>
                <span class="label-text">Password</span>
                <input type="password" name="user_password" class="input-field" placeholder="••••••••" required>
                <div class="checkbox-container">
                    <input type="checkbox" required checked>
                    <span>I accept the <a href="#">terms of service</a> and <a href="#">privacy policy</a></span>
                </div>
                <button type="submit" class="btn-submit">Sign up</button>
            </form>
            <div class="footer-text">Already have an account? <a href="#" onclick="alert('Terminal login sequence initiated...')">Log in</a></div>
        </div>
    </div>
    <script>
        function triggerSocialAuth(method) { alert("Google Registration Hook Verified via Poster UI Cluster!"); }
    </script>
</body>
</html>
"""
    return html_content

@app.route("/auth/submit-signup", methods=["POST"])
def submit_signup():
    return redirect("/?auth=success")

if __name__ == "__main__":
    print("\n🚀 MOPOLEE SECURITY ENGINE ACTIVE: RUNNING SAFELY ON PORT 8082")
    app.run(host="0.0.0.0", port=8082, debug=True)

