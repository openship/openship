import {
  ChevronRight,
  Github,
  Box,
  Code,
  Bell,
  Grid,
  BarChart3,
  Settings,
  Globe,
  Layers,
} from "lucide-react";
import { CarrierNetwork } from "@karrio/console/components/features-illustrations/carrier-network";
import { FeatureShowcase } from "@karrio/console/components/feature-showcase";
import { CodePreview } from "@karrio/console/components/code-preview";
import { FeatureTabs } from "@karrio/console/components/feature-tabs";
import { CTASection } from "@karrio/console/components/cta-section";
import { Button } from "@karrio/insiders/components/ui/button";
import { auth } from "@karrio/console/apis/auth";
import Image from "next/image";
import Link from "next/link";

export default async function LandingPage() {
  const session = await auth();

  return (
    <div className="min-h-screen bg-[#0f0826] text-white">
      {/* Header */}
      <header className="sticky top-0 z-50 border-b border-white/10 bg-gradient-to-r from-[#0f0826] via-[#1a103d] to-[#0f0826] backdrop-blur-sm">
        <div className="container mx-auto px-4 max-w-[95%] xl:max-w-[1280px]">
          <nav className="h-16 flex items-center justify-between">
            <div className="flex items-center space-x-8">
              <Link href="/" className="flex items-center space-x-2">
                <Image
                  src="/logo.svg"
                  alt="Karrio Logo"
                  width={100}
                  height={30}
                />
              </Link>
              <div className="hidden md:flex space-x-8">
                <Link
                  href="https://docs.karrio.io"
                  className="text-white/80 hover:text-white transition-colors"
                >
                  Docs
                </Link>
                <Link
                  href="https://karrio.io/blog"
                  className="text-white/80 hover:text-white transition-colors"
                >
                  Blog
                </Link>
                <Link
                  href="https://docs.karrio.io/carriers/"
                  className="text-white/80 hover:text-white transition-colors"
                >
                  Carriers
                </Link>
                <Link
                  href="https://docs.karrio.io/insiders"
                  className="text-white/80 hover:text-white transition-colors"
                >
                  Insiders
                </Link>
              </div>
            </div>
            <div className="flex items-center space-x-4">
              <Link
                href="https://github.com/karrioapi"
                className="text-white/80 hover:text-white"
              >
                <Github className="h-6 w-6" />
              </Link>
              <Button className="bg-[#5722cc] hover:bg-[#5722cc]/90">
                <Link href={session?.user ? "/orgs" : "/signin"}>
                  {session?.user ? "Dashboard" : "Sign In"}
                </Link>
              </Button>
            </div>
          </nav>
        </div>
      </header>

      {/* Hero Section */}
      <section className="relative overflow-hidden pt-24 pb-16">
        <div className="absolute inset-0 bg-[radial-gradient(circle_at_top_right,#5722cc1a,transparent_50%),radial-gradient(circle_at_bottom_left,#79e5dd1a,transparent_50%)]" />
        <div className="absolute inset-0 bg-[conic-gradient(from_90deg_at_50%_50%,#0f082600,#5722cc0d,#79e5dd0d,#ff48000d,#0f082600)]" />
        <div className="absolute inset-0 backdrop-blur-[100px]" />
        <div className="container mx-auto px-4 relative max-w-[95%] xl:max-w-[1280px]">
          <div className="text-center space-y-8">
            <div className="inline-flex items-center rounded-full border border-white/10 bg-white/5 px-3 py-1 text-sm backdrop-blur-sm">
              <span className="rounded-full bg-[#ff4800] px-1.5 py-0.5 text-xs font-medium text-white mr-2">
                New
              </span>
              Karrio v2.0 is now live
            </div>
            <h1 className="text-4xl md:text-6xl font-bold bg-gradient-to-r from-white via-[#79e5dd] to-[#ff4800] bg-clip-text text-transparent pb-2">
              Modern Logistics, Redefined.
            </h1>
            <p className="text-lg md:text-xl text-white/80 max-w-2xl mx-auto">
              Empowering engineers, retailers, and logistics providers with
              cutting-edge shipping tools. Karrio is your platform for smarter
              integrations, streamlined operations, and scalable logistics.
            </p>
            <div className="flex flex-col sm:flex-row items-center justify-center gap-4">
              <Button size="lg" className="bg-[#5722cc] hover:bg-[#5722cc]/90">
                Get Started Free
                <ChevronRight className="ml-2 h-4 w-4" />
              </Button>
              <Button
                size="lg"
                variant="outline"
                className="border-[#79e5dd] text-[#79e5dd] hover:bg-[#79e5dd]/10"
              >
                Explore the Platform
              </Button>
            </div>
          </div>

          {/* Feature Tabs */}
          <div className="mt-16 py-16">
            <div className="mx-auto relative w-full">
              <FeatureTabs
                tabs={[
                  {
                    icon: <Globe className="h-5 w-5" />,
                    label: "Logistics Network",
                    value: "logistics-network",
                    title: "Extensible carrier network",
                    description:
                      "Manage and connect with multiple carriers through a single, unified platform with advanced connection management capabilities.",
                    features: [
                      "Centralized carrier connection management",
                      "Automated carrier credential handling",
                      "Carrier-specific configuration APIs",
                      "Easy onboarding for new carriers",
                    ],
                    demo: (
                      <div className="aspect-[3/1] relative flex justify-center items-center">
                        <Image
                          src="/carrier-connection.svg"
                          alt="Tracking API interface demo"
                          width={1200}
                          height={400}
                          className="object-cover rounded-lg"
                        />
                      </div>
                    ),
                  },
                  {
                    icon: <Code className="h-5 w-5" />,
                    label: "Shipping Integration",
                    value: "shipping-integration",
                    title: "Unified shipping API",
                    description:
                      "Access a powerful set of APIs for end-to-end shipping operations, from rate comparison to label generation and shipment management.",
                    features: [
                      "Real-time multi-carrier rate fetching API",
                      "Efficient label generation API with customization options",
                      "Complete shipment lifecycle management API",
                      "Seamless integration with major carriers worldwide",
                    ],
                    demo: (
                      <div className="aspect-[3/1] relative flex justify-center items-center">
                        <Image
                          src="/placeholder.svg"
                          alt="Shipping API interface demo"
                          width={1200}
                          height={400}
                          className="object-cover rounded-lg"
                        />
                      </div>
                    ),
                  },
                  {
                    icon: <Bell className="h-5 w-5" />,
                    label: "Real-time Tracking",
                    value: "real-time-tracking",
                    title: "End-to-end data visibility",
                    description:
                      "Stay informed with comprehensive tracking capabilities and automated updates for all your shipments across carriers.",
                    features: [
                      "Unified tracking API for all carriers",
                      "Automated background tracking updates",
                      "Real-time webhook notifications",
                      "Detailed tracking event history",
                    ],
                    demo: (
                      <div className="aspect-[3/1] relative flex justify-center items-center">
                        <Image
                          src="/placeholder.svg"
                          alt="Tracking API interface demo"
                          width={1200}
                          height={400}
                          className="object-cover rounded-lg"
                        />
                      </div>
                    ),
                  },
                  {
                    icon: <Layers className="h-5 w-5" />,
                    label: "Document Generation",
                    value: "document-generation",
                    title: "Customizable document generation",
                    description:
                      "Create and customize shipping documents with a powerful templating engine that supports various document types and formats.",
                    features: [
                      "Custom document generation API",
                      "Advanced label design templating",
                      "GS1-compliant shipping document generation",
                      "Flexible invoice and customs documentation",
                    ],
                    demo: (
                      <div className="aspect-[3/1] relative flex justify-center items-center">
                        <Image
                          src="/placeholder.svg"
                          alt="Document Generation interface demo"
                          width={1200}
                          height={400}
                          className="object-cover rounded-lg"
                        />
                      </div>
                    ),
                  },
                  {
                    icon: <Settings className="h-5 w-5" />,
                    label: "Automation",
                    value: "automation",
                    title: "Logistics automation",
                    description:
                      "Automate your logistics operations with intelligent shipping rules and customizable fulfillment workflows.",
                    features: [
                      "Customizable shipping rules engine",
                      "Automated fulfillment workflows",
                      "Smart carrier selection",
                      "Conditional routing and processing",
                    ],
                    demo: (
                      <div className="aspect-[3/1] relative flex justify-center items-center">
                        <Image
                          src="/placeholder.svg"
                          alt="Logistics Automation interface demo"
                          width={1200}
                          height={400}
                          className="object-cover rounded-lg"
                        />
                      </div>
                    ),
                  },
                ]}
              />
            </div>
          </div>
        </div>
      </section>

      {/* Value Proposition Section */}
      <section className="py-24 relative">
        <div className="absolute inset-0 bg-[radial-gradient(ellipse_at_top,#5722cc0d,transparent_50%)]" />
        <div className="absolute inset-0 bg-[conic-gradient(from_180deg_at_50%_50%,#0f082600,#79e5dd0d,#0f082600)]" />
        <div className="absolute inset-0 backdrop-blur-[100px]" />
        <div className="container mx-auto px-4 relative max-w-[95%] xl:max-w-[1280px]">
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-8 lg:gap-12">
            <div className="space-y-3">
              <div className="w-10 h-10 rounded-lg bg-[#79e5dd]/10 flex items-center justify-center">
                <Box className="w-5 h-5 text-[#79e5dd]" />
              </div>
              <h3 className="text-lg font-semibold">Launch in days</h3>
              <p className="text-sm text-white/60 leading-relaxed">
                Use Karrio's hosted or embedded functionality to go live faster,
                and avoid the up-front costs and development time usually
                required for shipping integration.
              </p>
            </div>
            <div className="space-y-3">
              <div className="w-10 h-10 rounded-lg bg-[#79e5dd]/10 flex items-center justify-center">
                <BarChart3 className="w-5 h-5 text-[#79e5dd]" />
              </div>
              <h3 className="text-lg font-semibold">
                Manage shipping at scale
              </h3>
              <p className="text-sm text-white/60 leading-relaxed">
                Use tooling and services from Karrio so you don't have to
                dedicate extra resources to carrier integration, rate
                optimization, or compliance management.
              </p>
            </div>
            <div className="space-y-3">
              <div className="w-10 h-10 rounded-lg bg-[#79e5dd]/10 flex items-center justify-center">
                <Globe className="w-5 h-5 text-[#79e5dd]" />
              </div>
              <h3 className="text-lg font-semibold">Ship globally</h3>
              <p className="text-sm text-white/60 leading-relaxed">
                Help your users reach more customers worldwide with local
                carrier integrations and the ability to easily calculate duties,
                taxes, and customs documentation.
              </p>
            </div>
            <div className="space-y-3">
              <div className="w-10 h-10 rounded-lg bg-[#79e5dd]/10 flex items-center justify-center">
                <Layers className="w-5 h-5 text-[#79e5dd]" />
              </div>
              <h3 className="text-lg font-semibold">
                Build new revenue streams
              </h3>
              <p className="text-sm text-white/60 leading-relaxed">
                Optimize shipping revenue by collecting fees on each
                transaction. Monetize Karrio's capabilities by enabling premium
                features, automated workflows, and value-added services.
              </p>
            </div>
          </div>
          <div className="mt-20 text-center space-y-3">
            <div className="text-[#79e5dd] text-base font-medium">
              Ship with confidence
            </div>
            <h2 className="text-3xl md:text-4xl font-bold">
              Build a foundation for any logistics business
            </h2>
          </div>
        </div>
      </section>

      {/* How It Works Section */}
      <section className="py-24 relative overflow-hidden">
        <div className="absolute inset-0 bg-[radial-gradient(circle_at_bottom_right,#ff48001a,transparent_70%)]" />
        <div className="absolute inset-0 bg-[conic-gradient(from_270deg_at_50%_50%,#0f082600,#5722cc0d,#79e5dd0d,#0f082600)]" />
        <div className="absolute inset-0 backdrop-blur-[100px]" />
        <div className="container mx-auto px-4 relative max-w-[95%] xl:max-w-[1280px]">
          <div className="mb-16">
            <div className="text-[#79e5dd] mb-4">How it works</div>
            <h2 className="text-3xl md:text-5xl font-bold mb-4">
              Build your shipping operations with speed and flexibility
            </h2>
            <p className="text-white/60 max-w-3xl">
              Offer your users a great experience from day one with fast
              onboarding, accurate dashboards, and useful workflows – such as
              returns, tracking notifications, and carrier management.
            </p>
          </div>
          <div className="space-y-12">
            <FeatureShowcase
              title="Shipping Integration"
              description="Minimize the complexity associated with building your own carrier integrations and shipping workflows."
              learnMoreHref="#"
              tabs={[
                {
                  label: "Hosted",
                  value: "hosted",
                  content: (
                    <div className="bg-black/20 aspect-video rounded-lg overflow-hidden">
                      <Image
                        src="/placeholder.svg"
                        width={800}
                        height={400}
                        alt="Karrio hosted shipping interface"
                        className="w-full h-full object-cover"
                      />
                    </div>
                  ),
                },
                {
                  label: "Embedded",
                  value: "embedded",
                  content: (
                    <div className="bg-black/20 aspect-video rounded-lg overflow-hidden">
                      <Image
                        src="/placeholder.svg"
                        width={800}
                        height={400}
                        alt="Karrio embedded shipping components"
                        className="w-full h-full object-cover"
                      />
                    </div>
                  ),
                },
                {
                  label: "API",
                  value: "api",
                  content: (
                    <div className="flex justify-center">
                      <div className="bg-black/20 rounded-lg p-4 w-[800px] h-[400px] overflow-auto">
                        <pre className="text-sm text-white/90">
                          <code>{`// Create a new shipment
const shipment = await karrio.shipments.create({
  service: "fedex_ground",
  shipper: {
    company_name: "ACME Inc",
    address_line1: "123 Shipping St",
    postal_code: "V6M2V9",
    city: "Vancouver",
    country_code: "CA",
  },
  recipient: {
    name: "John Doe",
    address_line1: "456 Delivery Ave",
    postal_code: "27401",
    city: "Greensboro",
    country_code: "US",
  },
  parcels: [{
    weight: 1.5,
    weight_unit: "KG",
    width: 20,
    height: 10,
    length: 15,
    dimension_unit: "CM"
  }]
});`}</code>
                        </pre>
                      </div>
                    </div>
                  ),
                },
              ]}
            />
            <FeatureShowcase
              title="Shipment Dashboard"
              description="Add dashboard functionality to your website in minutes. Share important details such as tracking status and delivery estimates – all while supporting complex workflows such as returns and customs documentation."
              learnMoreHref="#"
              tabs={[
                {
                  label: "Hosted",
                  value: "hosted",
                  content: (
                    <div className="bg-black/20 aspect-video rounded-lg overflow-hidden">
                      <Image
                        src="/placeholder.svg"
                        width={800}
                        height={400}
                        alt="Karrio hosted dashboard"
                        className="w-full h-full object-cover"
                      />
                    </div>
                  ),
                },
                {
                  label: "Embedded",
                  value: "embedded",
                  content: (
                    <div className="bg-black/20 aspect-video rounded-lg overflow-hidden">
                      <Image
                        src="/placeholder.svg"
                        width={800}
                        height={400}
                        alt="Karrio embedded dashboard components"
                        className="w-full h-full object-cover"
                      />
                    </div>
                  ),
                },
                {
                  label: "API",
                  value: "api",
                  content: (
                    <div className="flex justify-center">
                      <div className="bg-black/20 rounded-lg p-4 w-[800px] h-[400px] overflow-auto">
                        <pre className="text-sm text-white/90">
                          <code>{`// Fetch shipment details and tracking
const shipment = await karrio.shipments.retrieve('shp_123');
const tracking = await karrio.tracking.get(shipment.tracking_number);

console.log(tracking.status); // "in_transit"
console.log(tracking.estimated_delivery); // "2024-01-28"
console.log(tracking.events); // Array of tracking events`}</code>
                        </pre>
                      </div>
                    </div>
                  ),
                },
              ]}
            />
            <FeatureShowcase
              title="Carrier Account Management"
              description="Easily manage and integrate multiple carrier accounts, streamlining your shipping operations and providing flexibility for your customers."
              learnMoreHref="#"
              tabs={[
                {
                  label: "Hosted",
                  value: "hosted",
                  content: (
                    <div className="bg-black/20 aspect-video rounded-lg overflow-hidden">
                      <Image
                        src="/placeholder.svg"
                        width={800}
                        height={400}
                        alt="Karrio hosted carrier account management"
                        className="w-full h-full object-cover"
                      />
                    </div>
                  ),
                },
                {
                  label: "Embedded",
                  value: "embedded",
                  content: (
                    <div className="bg-black/20 aspect-video rounded-lg overflow-hidden">
                      <Image
                        src="/placeholder.svg"
                        width={800}
                        height={400}
                        alt="Karrio embedded carrier account components"
                        className="w-full h-full object-cover"
                      />
                    </div>
                  ),
                },
                {
                  label: "API",
                  value: "api",
                  content: (
                    <div className="flex justify-center">
                      <div className="bg-black/20 rounded-lg p-4 w-[800px] h-[400px] overflow-auto">
                        <pre className="text-sm text-white/90">
                          <code>{`// Add a new carrier account
const carrierAccount = await karrio.carrierAccounts.create({
  carrier: "fedex",
  account_number: "123456789",
  account_country: "US",
  test_mode: false,
  active: true,
  credentials: {
    user_key: "YOUR_FEDEX_USER_KEY",
    password: "YOUR_FEDEX_PASSWORD",
    meter_number: "YOUR_FEDEX_METER_NUMBER",
    account_number: "YOUR_FEDEX_ACCOUNT_NUMBER"
  }
});

console.log(carrierAccount.id); // "ca_123456789"
console.log(carrierAccount.status); // "active"`}</code>
                        </pre>
                      </div>
                    </div>
                  ),
                },
              ]}
            />
          </div>
        </div>
      </section>

      {/* Developers Section */}
      <section className="py-24 relative">
        <div className="absolute inset-0 bg-[radial-gradient(circle_at_center,#5722cc1a,transparent_70%)]" />
        <div className="absolute inset-0 bg-[conic-gradient(from_0deg_at_50%_50%,#0f082600,#79e5dd0d,#0f082600)]" />
        <div className="absolute inset-0 backdrop-blur-[100px]" />
        <div className="container mx-auto px-4 relative max-w-[95%] xl:max-w-[1280px]">
          <div className="text-center mb-8">
            <div className="text-[#79e5dd] mb-4">Developer-first design</div>
            <h2 className="text-3xl md:text-5xl font-bold mb-4">
              A unified platform with modern APIs
            </h2>
            <p className="text-white/60 max-w-2xl mx-auto">
              Karrio provides a single, elegant interface that abstracts dozens
              of carrier integrations.
            </p>
          </div>
          <div className="grid lg:grid-cols-2 gap-12 mt-16">
            <div className="space-y-12">
              <div className="flex gap-4">
                <div className="flex-shrink-0">
                  <div className="w-12 h-12 rounded-lg bg-white/5 flex items-center justify-center">
                    <Code className="w-6 h-6 text-[#79e5dd]" />
                  </div>
                </div>
                <div>
                  <h3 className="font-semibold mb-2">
                    RESTful APIs, JSON responses
                  </h3>
                  <p className="text-white/60">
                    Modern API design with predictable resource-oriented URLs
                    and JSON responses.
                  </p>
                </div>
              </div>
              <div className="flex gap-4">
                <div className="flex-shrink-0">
                  <div className="w-12 h-12 rounded-lg bg-white/5 flex items-center justify-center">
                    <Box className="w-6 h-6 text-[#79e5dd]" />
                  </div>
                </div>
                <div>
                  <h3 className="font-semibold mb-2">
                    Seamless dashboard integration
                  </h3>
                  <p className="text-white/60">
                    Integrate Karrio into your application with our ready-to-use
                    components.
                  </p>
                </div>
              </div>
              <div className="flex gap-4">
                <div className="flex-shrink-0">
                  <div className="w-12 h-12 rounded-lg bg-white/5 flex items-center justify-center">
                    <Bell className="w-6 h-6 text-[#79e5dd]" />
                  </div>
                </div>
                <div>
                  <h3 className="font-semibold mb-2">
                    Real-time webhook events
                  </h3>
                  <p className="text-white/60">
                    Get instant updates for shipment status changes and tracking
                    events.
                  </p>
                </div>
              </div>
              <div className="flex gap-4">
                <div className="flex-shrink-0">
                  <div className="w-12 h-12 rounded-lg bg-white/5 flex items-center justify-center">
                    <Grid className="w-6 h-6 text-[#79e5dd]" />
                  </div>
                </div>
                <div>
                  <h3 className="font-semibold mb-2">Multi-carrier support</h3>
                  <p className="text-white/60">
                    Connect with 30+ carriers through a single integration
                    point.
                  </p>
                </div>
              </div>
              <div className="flex flex-col sm:flex-row items-start gap-4">
                <Button
                  variant="outline"
                  className="bg-[#79e5dd] text-[#1f1834] hover:bg-[#79e5dd]/90"
                >
                  Read the docs
                </Button>
                <Button
                  variant="outline"
                  className="border-white/20 hover:bg-white/10"
                >
                  Get your API key
                </Button>
              </div>
            </div>
            <div className="lg:mt-0 mt-8">
              <CodePreview
                languages={[
                  {
                    label: "Node.js",
                    value: "nodejs",
                    code: `// Get a shipment rate and create a label
import { Karrio } from '@karrio/sdk';

const karrio = new Karrio('sk_test_123456789');

const shipment = await karrio.shipments.create({
  service: "usps_priority",
  shipper: {
    postal_code: "V6M2V9",
    country_code: "CA",
  },
  recipient: {
    postal_code: "27401",
    country_code: "US",
  },
  parcels: [{
    weight: 1,
    width: 10,
    height: 10,
    length: 10,
  }]
});`,
                    response: `{
  "id": "shp_f8f8f8f8f8f8f8f8",
  "status": "created",
  "tracking_number": "9400100000000000000000",
  "label_url": "https://api.karrio.io/v1/labels/shp_f8f8f8f8",
  "tracking_url": "https://track.karrio.io/shp_f8f8f8f8",
  "created_at": "2024-01-01T00:00:00Z"
}`,
                  },
                  {
                    label: "Python",
                    value: "python",
                    code: `# Get a shipment rate and create a label
from karrio import Karrio

karrio = Karrio('sk_test_123456789')

shipment = karrio.shipments.create(
    service="usps_priority",
    shipper={
        "postal_code": "V6M2V9",
        "country_code": "CA",
    },
    recipient={
        "postal_code": "27401",
        "country_code": "US",
    },
    parcels=[{
        "weight": 1,
        "width": 10,
        "height": 10,
        "length": 10,
    }]
)`,
                    response: `{
  "id": "shp_f8f8f8f8f8f8f8f8",
  "status": "created",
  "tracking_number": "9400100000000000000000",
  "label_url": "https://api.karrio.io/v1/labels/shp_f8f8f8f8",
  "tracking_url": "https://track.karrio.io/shp_f8f8f8f8",
  "created_at": "2024-01-01T00:00:00Z"
}`,
                  },
                ]}
              />
            </div>
          </div>
        </div>
      </section>

      {/* CTA Section */}
      <CTASection />

      {/* Footer */}
      <footer className="border-t border-white/10 py-12">
        <div className="container mx-auto px-4 max-w-[95%] xl:max-w-[1140px]">
          <div className="grid grid-cols-2 md:grid-cols-5 gap-8">
            <div className="col-span-2 md:col-span-1">
              <Link href="/" className="flex items-center space-x-2">
                <Image
                  src="/logo.svg"
                  alt="Karrio Logo"
                  width={132}
                  height={32}
                />
              </Link>
            </div>
            <div>
              <h4 className="font-bold mb-4">Product</h4>
              <ul className="space-y-2">
                <li>
                  <Link href="#" className="text-white/60 hover:text-white">
                    Features
                  </Link>
                </li>
                <li>
                  <Link href="#" className="text-white/60 hover:text-white">
                    Documentation
                  </Link>
                </li>
                <li>
                  <Link href="#" className="text-white/60 hover:text-white">
                    API Reference
                  </Link>
                </li>
              </ul>
            </div>
            <div>
              <h4 className="font-bold mb-4">Company</h4>
              <ul className="space-y-2">
                <li>
                  <Link href="#" className="text-white/60 hover:text-white">
                    About
                  </Link>
                </li>
                <li>
                  <Link href="#" className="text-white/60 hover:text-white">
                    Blog
                  </Link>
                </li>
                <li>
                  <Link href="#" className="text-white/60 hover:text-white">
                    Careers
                  </Link>
                </li>
              </ul>
            </div>
            <div>
              <h4 className="font-bold mb-4">Resources</h4>
              <ul className="space-y-2">
                <li>
                  <Link href="#" className="text-white/60 hover:text-white">
                    Community
                  </Link>
                </li>
                <li>
                  <Link href="#" className="text-white/60 hover:text-white">
                    Contact
                  </Link>
                </li>
                <li>
                  <Link href="#" className="text-white/60 hover:text-white">
                    Privacy Policy
                  </Link>
                </li>
              </ul>
            </div>
            <div>
              <h4 className="font-bold mb-4">Legal</h4>
              <ul className="space-y-2">
                <li>
                  <Link href="#" className="text-white/60 hover:text-white">
                    Terms
                  </Link>
                </li>
                <li>
                  <Link href="#" className="text-white/60 hover:text-white">
                    Privacy
                  </Link>
                </li>
                <li>
                  <Link href="#" className="text-white/60 hover:text-white">
                    Cookies
                  </Link>
                </li>
              </ul>
            </div>
          </div>
          <div className="mt-12 pt-8 border-t border-white/10 text-center text-white/60">
            <p>
              &copy; {new Date().getFullYear()} Karrio. All rights reserved.
            </p>
          </div>
        </div>
      </footer>
    </div>
  );
}