import { useQuery } from "@tanstack/react-query";

// Relative URL: the browser talks to its own origin and Vite proxies /api to the backend.
async function fetchPing(): Promise<{ ok: boolean }> {
  const res = await fetch("/api/v1/ping");
  if (!res.ok) throw new Error(`ping failed: ${res.status}`);
  return res.json();
}

export default function App() {
  const ping = useQuery({ queryKey: ["ping"], queryFn: fetchPing });

  const status = ping.isPending
    ? "checking…"
    : ping.data?.ok
      ? "ok"
      : "unreachable";

  return (
    <main className="flex min-h-screen flex-col items-center justify-center gap-2">
      <h1 className="text-xl font-semibold">Enterprise Intellect</h1>
      <p data-testid="api-status">API: {status}</p>
    </main>
  );
}
