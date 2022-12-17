/**
 * Add your config changes here.
 * @module config
 * @example
 * export default function applyConfig(config) {
 *   config.settings = {
 *     ...config.settings,
 *     port: 4300,
 *     listBlockTypes: {
 *       ...config.settings.listBlockTypes,
 *       'my-list-item',
 *    }
 * }
 */

// All your imports required for the config here BEFORE this line
import '@plone/volto/config';

export default function applyConfig(config) {
  console.warn("frontend/src/config.js");
  config.settings = {
    ...config.settings,
    isMultilingual: false,
    supportedLanguages: ['en'],
    defaultLanguage: 'en',
  };

  // Re-enable non-GDPR compliant blocks, inhibited by @eeacms/volto-eea-kitkat:
  config.blocks.blocksConfig.video.restricted = false;
  config.blocks.blocksConfig.maps.restricted = false;
  config.blocks.blocksConfig.html.restricted = false;

  // https://github.com/plone/volto/blob/621c5a727a0f3d9a03cbf58b64bd94c5d8834147/CHANGELOG.md#1600-alpha53-2022-11-18
  // Experimental setting to move the button for adding a new block to show
  // below any selected block, instead of only on the left of empty text
  // blocks.
  config.experimental.addBlockButton.enabled = true;

  // https://6.dev-docs.plone.org/volto/configuration/workingcopy.html
  config.settings.hasWorkingCopySupport = true;
  return config;
}
