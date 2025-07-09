# Real-Time-Healthcare-Monitoring-System

<h3>🚀 Overview</h3>
<p>
A real-time healthcare data monitoring system that simulates, processes, and stores patient vitals for live tracking and historical analysis.
</p>

<h3>🛠️ Tech Stack</h3>
<p><strong>PySpark</strong>, <strong>Apache Kafka</strong>, <strong>Spring Boot</strong>, <strong>PostgreSQL</strong>, <strong>Thymeleaf</strong></p>

<h3>📌 Features</h3>
<ul>
  <li>Simulates real-time vitals data (heart rate, temperature, BP, etc.) via a Python script and publishes it to Kafka.</li>
  <li>Uses <strong>PySpark Streaming</strong> to consume and process data — including risk classification and timestamp formatting.</li>
  <li>A <strong>Spring Boot microservice</strong> consumes the enriched data and stores it in a <strong>PostgreSQL</strong> database.</li>
  <li><strong>Admin panel</strong> for managing patients and doctors, and <strong>Doctor dashboard</strong> to view real-time and historical vitals via Thymeleaf.</li>
  <li>Designed with <strong>MVC architecture</strong> and scalable endpoints.</li>
</ul>

<h3>📈 Impact</h3>
<p>Achieved ~30% improvement in real-time risk detection and data flow efficiency through optimized streaming and processing logic.</p>
