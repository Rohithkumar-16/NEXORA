import { useState } from "react";
import { useNavigate } from "react-router-dom";
import "./Login.css";

function Login() {
  const navigate = useNavigate();
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  const handleSubmit = (event) => {
    event.preventDefault();

    console.log("LOGIN DATA:", {
      email,
      password,
    });

    alert("Login submitted!");
  };

  return (
    <div className="login-page">
      {/* NAVBAR */}

      <nav className="login-navbar">
        <a href="/" className="login-logo">
          NEXORA<span>.</span>
        </a>

        <a href="/" className="login-back">
          ← Back to NEXORA
        </a>
      </nav>

      {/* LOGIN CARD */}

      <main className="login-container">
        <div className="login-badge">NEXORA • STUDENT ACCESS</div>

        <h1>
          Welcome <span>back.</span>
        </h1>

        <p className="login-description">
          Sign in to continue building your profile, discovering projects and
          connecting with students.
        </p>

        <form className="login-form" onSubmit={handleSubmit}>
          {/* EMAIL */}

          <div className="login-field">
            <label htmlFor="email">Email Address</label>

            <input
              id="email"
              type="email"
              value={email}
              onChange={(event) => setEmail(event.target.value)}
              placeholder="Enter your email"
              required
            />
          </div>

          {/* PASSWORD */}

          <div className="login-field">
            <label htmlFor="password">Password</label>

            <input
              id="password"
              type="password"
              value={password}
              onChange={(event) => setPassword(event.target.value)}
              placeholder="Enter your password"
              required
            />
          </div>

          {/* FORGOT PASSWORD */}

          <div className="login-options">
            <a href="/forgot-password">Forgot password?</a>
          </div>

          {/* LOGIN BUTTON */}

          <button type="submit" className="login-button">
            Sign In
            <span>→</span>
          </button>
        </form>

        {/* SIGN UP */}

        <div className="login-signup">
          Don't have an account?
          <a href="/signup"> Create one →</a>
        </div>
      </main>
    </div>
  );
}

export default Login;
