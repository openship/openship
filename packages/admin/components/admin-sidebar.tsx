"use client";

import {
  Box,
  Building2,
  Clock,
  FileText,
  LayoutDashboard,
  Truck,
  Users,
} from "lucide-react";
import { cn } from "@karrio/insiders/lib/utils";
import Link from "next/link";
import { usePathname } from "next/navigation";

const menuItems = [
  {
    label: "Platform details",
    icon: LayoutDashboard,
    href: "/admin",
  },
  {
    label: "Carrier connections",
    icon: Truck,
    href: "/admin/carrier-connections",
  },
  {
    label: "Users and permissions",
    icon: Users,
    href: "/admin/users-permissions",
  },
  {
    label: "Organization accounts",
    icon: Building2,
    href: "/admin/organization-accounts",
  },
  {
    label: "Surcharge and discounts",
    icon: FileText,
    href: "/admin/surcharges",
  },
  {
    label: "Platform activity log",
    icon: Clock,
    href: "/admin/activity",
    isDisabled: true,
  },
];

export function AdminSidebar() {
  const pathname = usePathname();
  const basePath = pathname?.split("/admin")[0] || "";

  return (
    <div className="sticky top-4 rounded-lg border bg-white shadow-sm">
      <div className="flex h-14 items-center gap-3 border-b px-4">
        <div className="flex h-8 w-8 items-center justify-center rounded bg-primary">
          <Box className="h-5 w-5 text-white" />
        </div>
        <div className="flex flex-col">
          <span className="text-sm font-medium">Karrio</span>
          <span className="text-xs text-muted-foreground">localhost:3000</span>
        </div>
      </div>
      <div className="max-h-[calc(100vh-120px)] overflow-y-auto px-2 py-4">
        {menuItems.map((item) => (
          <Link
            key={item.label}
            href={`${basePath}${item.href}`}
            className={cn(
              "flex items-center gap-3 rounded-md px-2 py-2 text-sm text-gray-700 hover:bg-gray-100",
              "focus-visible:bg-gray-100 focus-visible:outline-none",
              pathname === `${basePath}${item.href}` &&
              "bg-gray-100 font-medium",
              item.isDisabled && "pointer-events-none opacity-50",
            )}
          >
            <item.icon className="h-4 w-4" />
            {item.label}
          </Link>
        ))}
      </div>
    </div>
  );
}
