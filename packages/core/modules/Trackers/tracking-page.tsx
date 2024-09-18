import { TrackingEvent, TrackingStatus } from "@karrio/types/rest/api";
import { formatDayDate, isNone, KARRIO_API, url$ } from "@karrio/lib";
import { dynamicMetadata } from "@karrio/core/components/metadata";
import { Collection, KarrioClient } from "@karrio/types";
import { loadMetadata } from "@karrio/core/context/main";
import Link from "next/link";
import React from "react";
import TrackingHeader from "@karrio/core/components/TrackingHeader";
import TrackingEvents from "@karrio/core/components/TrackingEvents";
import TrackingMessages from "@karrio/core/components/TrackingMessages";

export const generateMetadata = dynamicMetadata("Tracking");

type DayEvents = { [k: string]: TrackingEvent[] };

export default async function Page({ params }: { params: Collection }) {
  const id = params?.id as string;
  const { metadata } = await loadMetadata();
  const client = new KarrioClient({
    basePath: url$`${(metadata?.HOST as string) || KARRIO_API}`,
  });
  const { data: tracker, message } = await client.trackers
    .retrieve({ idOrTrackingNumber: id })
    .then(({ data }) => ({ data, message: null }))
    .catch((_) => {
      console.log(_.response?.data?.errors || _.response);
      return {
        data: null,
        message: `No Tracker ID nor Tracking Number found for ${id}`,
      };
    });

  const computeEvents = (tracker: TrackingStatus): DayEvents => {
    return (tracker?.events || []).reduce((days, event: TrackingEvent) => {
      const daydate = formatDayDate(event.date as string);
      return { ...days, [daydate]: [...(days[daydate] || []), event] };
    }, {} as DayEvents);
  };

  return (
    <>
      <section className="hero is-fullheight p-2">
        <div className="container">
          <div className="has-text-centered my-4">
            <Link legacyBehavior href="/">
              <span className="is-size-4 has-text-primary has-text-weight-bold is-lowercase">
                {metadata?.APP_NAME}
              </span>
            </Link>
          </div>

          {!isNone(tracker) && (
            <>
              <div className="card isolated-card">
                <div className="card-content">
                  <TrackingHeader tracker={tracker as TrackingType} />
                </div>

                <footer className="card-footer"></footer>
              </div>

              <hr />
              
              <TrackingEvents tracker={tracker as TrackingType} />
            </>
          )}

          <TrackingMessages messages={tracker?.messages || [] } />
          
          {!isNone(message) && (
            <div className="card isolated-card my-6">
              <div className="card-content has-text-centered ">
                <p>{message}</p>
              </div>
            </div>
          )}
        </div>

        <hr className="mt-4" />

        <div className="hero-footer mb-4">
          <div className="content has-text-centered">
            <p>
              <Link legacyBehavior href="/" className="button is-white">
                <span>Powered by &copy; {metadata?.APP_NAME}</span>
              </Link>
            </p>
          </div>
        </div>
      </section>
    </>
  );
}
