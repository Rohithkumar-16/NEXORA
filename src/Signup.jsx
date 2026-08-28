import { useState } from "react";
import { useNavigate } from "react-router-dom";
import "./Signup.css";

function Signup() {
  const navigate = useNavigate();
  const [formData, setFormData] = useState({
    name: "",
    email: "",
    password: "",
    confirmPassword: "",
  });

  const handleChange = (event) => {
    const { name, value } = event.target;

    setFormData((previous) => ({
      ...previous,
      [name]: value,
    }));
  };

  const handleSubmit = (event) => {
    event.preventDefault();

    if (formData.password !== formData.confirmPassword) {
      alert("Passwords do not match!");
      return;
    }

    console.log("SIGNUP DATA:", formData);

    alert("Account created successfully!");

    navigate("/profile");
  };

  return (
    <div className="signup-page">
      {/* NAVBAR */}

      <nav className="signup-navbar">
        <a href="/" className="signup-logo">
          NEXORA<span>.</span>
        </a>

        <a href="/" className="signup-back">
          ← Back to NEXORA
        </a>
      </nav>

      {/* SIGNUP CONTAINER */}

      <main className="signup-container">
        <div className="signup-badge">NEXORA • JOIN THE COMMUNITY</div>

        <h1>
          Start building <span>together.</span>
        </h1>

        <p className="signup-description">
          Create your NEXORA account and connect with students, projects and
          opportunities that match your interests.
        </p>

        <form className="signup-form" onSubmit={handleSubmit}>
          {/* NAME */}

          <div className="signup-field">
            <label htmlFor="name">Full Name</label>

            <input
              id="name"
              type="text"
              name="name"
              value={formData.name}
              onChange={handleChange}
              placeholder="Enter your full name"
              required
            />
          </div>

          {/* EMAIL */}

          <div className="signup-field">
            <label htmlFor="email">Email Address</label>

            <input
              id="email"
              type="email"
              name="email"
              value={formData.email}
              onChange={handleChange}
              placeholder="Enter your email"
              required
            />
          </div>

          {/* PASSWORD */}

          <div className="signup-field">
            <label htmlFor="password">Password</label>

            <input
              id="password"
              type="password"
              name="password"
              value={formData.password}
              onChange={handleChange}
              placeholder="Create a password"
              required
              minLength="6"
            />
          </div>

          {/* CONFIRM PASSWORD */}

          <div className="signup-field">
            <label htmlFor="confirmPassword">Confirm Password</label>

            <input
              id="confirmPassword"
              type="password"
              name="confirmPassword"
              value={formData.confirmPassword}
              onChange={handleChange}
              placeholder="Confirm your password"
              required
              minLength="6"
            />
          </div>

          {/* TERMS */}

          <label className="signup-terms">
            <input type="checkbox" required />

            <span>
              I agree to the NEXORA terms and understand that my profile
              information may be visible to other students.
            </span>
          </label>

          {/* BUTTON */}

          <button type="submit" className="signup-button">
            Create Account
            <span>→</span>
          </button>
        </form>

        {/* LOGIN */}

        <div className="signup-login">
          Already have an account?
          <a href="/login"> Sign in →</a>
        </div>
      </main>
    </div>
  );
}

export default Signup;
