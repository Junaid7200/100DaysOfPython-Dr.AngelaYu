import React from 'react';
import { Timeline } from 'lucide-react';

const TSRTimeline = () => {
  const events = [
    { year: 1997, event: "de la Escalera et al.: Color thresholding and shape analysis" },
    { year: 2007, event: "Maldonado-Bascon et al.: SVM for TSR" },
    { year: 2010, event: "Soheilian et al.: 3D city models for TSR" },
    { year: 2011, event: "Sermanet & LeCun: Multi-scale CNN for TSR" },
    { year: 2012, event: "Krizhevsky et al.: AlexNet" },
    { year: 2014, event: "Simonyan & Zisserman: VGGNet" },
    { year: 2016, event: "He et al.: ResNet" },
    { year: 2018, event: "Arcos-García et al.: Inception-based TSR" }
  ];

  return (
    <div className="p-4 bg-white rounded-lg shadow">
      <h2 className="text-xl font-bold mb-4 flex items-center">
        <Timeline className="mr-2" /> TSR Development Timeline
      </h2>
      <ul className="space-y-2">
        {events.map((event, index) => (
          <li key={index} className="flex items-start">
            <div className="w-16 font-bold">{event.year}</div>
            <div className="flex-1">{event.event}</div>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default TSRTimeline;
